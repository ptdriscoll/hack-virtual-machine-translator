# -*- coding: utf-8 -*- 

"""
This class translates each VM command into assembly code. 
"""

import os

if os.getcwd().endswith('VMTranslator'):
    from vm_translator import assembly_code as asm
    
else:
    import assembly_code as asm


class CodeWriter:
    """
    Translates VM commands into assembly code.
    """
    
    def __init__(self, full_path):
        """
        Initializes virtual RAM for pointers and base address indices, 
        and, if write_to_file=True, opens output file/stream and prepares to write into it.
        """
        
        self._file_open = open(full_path, 'w')        
        self._current_file_name = ''
        self._current_function_name = 'Sys'
        self._jump_count = 0 
        self._return_count = 0        
        
        self._dispatch = {
            'C_ARITHMETIC': self.write_arithmetic,
            'C_PUSH': self.write_push_pop,
            'C_POP': self.write_push_pop,
            'C_LABEL': self.write_flow,
            'C_GOTO': self.write_flow,
            'C_IF': self.write_flow,
            'C_FUNCTION': self.write_function,
            'C_RETURN': self.write_return,
            'C_CALL': self.write_call    
        }
    
    def __str__(self):
        to_print =  '     Writing file: ' + self._current_file_name + '\n'
        to_print += ' Current function: ' + self._current_function_name + '\n'
        to_print += '       Jump count: ' + str(self._jump_count) + '\n'
        to_print += '     Return count: ' + str(self._return_count) + '\n'
        return to_print 
    
    def set_file_name(self, file_name):
        """
        Informs code writer that translation of a new VM file has started.
        """
        
        self._current_file_name = file_name 
        self._current_function_name = file_name #default until function declared         
        self._jump_count = 0
        self._return_count = 0
        
    def set_function_name(self, function_name):
        """
        Informs code writer that translation of a new VM file has started.
        """
        
        self._current_function_name = function_name 
        self._jump_count = 0   
        self._return_count = 0
        
    def write_init(self):
        """
        Writes assembly code that initializes VM, or boostraps code. 
        Code is placed at ROM[0]       
        """       
        
        note = '// Initialize stack pointer to 256\n'
        code = asm.assign_value_cmd('SP', '256') + '\n'       
        self._file_open.write(note + code) 
        self.write_call('call', 'Sys.init', '0')
        
    def write_arithmetic(self, command):
        """
        Writes assembly code that is a translation of given arithmetic command.
        """
        
        note = '// ' + self._current_function_name + ': ' + command + '\n'
       
        if command in ['add', 'sub', 'neg']:
            code = asm.math_cmd(asm.math_table[command])
            
        elif command in ['eq', 'gt', 'lt']:
            self._jump_count += 1
            jump = self._current_function_name + '$JUMP.' + str(self._jump_count)
            code = asm.compare_cmd(asm.math_table[command], jump)  

        #if command is an and, or, not      
        else:
            code = asm.logic_cmd(asm.math_table[command])     

        self._file_open.write(note + code + '\n')    
        return note + code + '\n'             
        
    def write_push_pop(self, command, segment, index, write=True):
        """
        Writes assembly code that is the translation of a given command, 
        where command is either:
        - C_PUSH
        - C_POP        
        """
        
        note = '// ' + self._current_function_name + ': ' 
        note += command + ' ' + segment + ' ' + index + '\n'
        
        static = False
        
        if segment == 'static':
            symbol = self._current_file_name 
            static = True            
            
        else:        
            symbol = asm.symbol_table[segment]   
        
        if command == 'pop':           
            code = asm.pop_cmd(symbol, index, static=static)    
        
        #if command == 'push'        
        else:
            code = asm.push_cmd(symbol, index, static=static)    
            
        if write:
            self._file_open.write(note + code + '\n') 
        return note + code + '\n'  
        
    def write_flow(self, command, label, note=True, write=True):
        """
        Writes assembly code that translates label command.       
        """  

        if label:
            label = self._current_function_name + '$' + label 
        
        #if no label, then it's a function, so declare as current_function_name 
        else:
            label = self._current_function_name
 
        if note:
            note = ' // ' + command        
        
        code = asm.flow_cmd(command, label, note=note) + '\n'

        if write:
            self._file_open.write(code) 
        return code 
        
    def write_function(self, command, function_name, num_locals):
        """
        Writes assembly code that translates function command.       
        """ 

        self.set_function_name(function_name)
        note = '// function ' + self._current_function_name + ' ' + num_locals + '\n'        
        
        code = self.write_flow('label', '', note=False, write=False)   

        for x in range(int(num_locals)):
            code += self.write_push_pop('push', 'constant', '0', write=False)
            #code += self.write_push_pop('pop', 'local', str(x), write=False)  

        self._file_open.write(note + code) 
        return note + code              

    def write_call(self, command, function_name, num_args):
        """
        Writes assembly code that translates call command. num_args is a string.      
        """
        
        note = '// call ' + function_name + ' ' + num_args + '\n'        
        
        #push return-address (using label below)
        self._return_count += 1
        return_address_label = self._current_function_name + '$return.' + str(self._return_count)
        code = asm.push_cmd('constant', return_address_label, note=' // push return-address\n\n') 
        
        #save LCL of calling function
        code += asm.push_cmd('R1', '0', note=' // push LCL\n\n') 
        
        #save ARG of calling function
        code += asm.push_cmd('R2', '0', note=' // push ARG\n\n') 
        
        #save THIS of calling function
        code += asm.push_cmd('R3', '0', note=' // push THIS\n\n') 
        
        #save THAT of calling function
        code += asm.push_cmd('R4', '0', note=' // push THAT\n\n') 
        
        #reposition ARG (n=number of args)
        steps_back = 0 - 5 - int(num_args)   
        code += asm.assign_cmd('ARG', 'SP', frame_steps=steps_back, note=' // ARG = SP-n-5\n\n')
        
        #reposition LCL
        code += asm.assign_cmd('LCL', 'SP', frame_steps=0, note=' // LCL = SP\n\n')
        
        #transfer control
        code += asm.flow_cmd('goto', function_name, note=' // goto f\n')        
        
        #label for return address        
        code += asm.flow_cmd('label', return_address_label, note=' // (return-address)\n') + '\n'        
        
        self._file_open.write(note + code) 
        return note + code

    def write_return(self, command):
        """
        Writes assembly code that translates return command.       
        """       
        
        note = '// ' + command + ' from ' + self._current_function_name + '\n' 
        
        #save endFrame address as temp variable
        code = asm.assign_cmd('R14', 'LCL', note=' // endFrame = LCL\n\n') 
        
        #save return address as another temp variable
        code += asm.assign_pointer_cmd('R15', 'R14', frame_steps=-5, note=' // retAddr = *(endFrame-5)\n\n')
        
        #Reposition return value for caller
        code += asm.pop_cmd('ARG', '0', note=' // *ARG = pop()\n\n')
        
        #Reposition SP of caller
        code += asm.assign_cmd('SP', 'ARG', frame_steps=1, note=' // SP = ARG+1\n\n')
        
        #Restore THAT of caller
        code += asm.assign_pointer_cmd('THAT', 'R14', frame_steps=-1, note=' // THAT = *(endFrame-1)\n\n')
        
        #Restore THIS of caller
        code += asm.assign_pointer_cmd('THIS', 'R14', frame_steps=-2, note=' // THIS = *(endFrame-2)\n\n')
        
        #Restore ARG of caller
        code += asm.assign_pointer_cmd('ARG', 'R14', frame_steps=-3, note=' // ARG = *(endFrame-3)\n\n')
        
        #Restore LCL of caller
        code += asm.assign_pointer_cmd('LCL', 'R14', frame_steps=-4, note=' // LCL = *(endFrame-4)\n\n')        
        
        #Jump to return address in caller
        code += asm.flow_cmd('goto', 'R15', note=' // goto retAddr\n')
        
        self._file_open.write(note + code) 
        return note + code           

    def write(self, command_type, args):
        """
        Uses command_type passed from parser to call correct write method 
        through self._dispatch mapping dictionary.                
        """        

        return self._dispatch[command_type](*args)        
        
    def close(self):
        """
        Closes output file.
        """
        
        self._file_open.close()
    
    
    
    
        
