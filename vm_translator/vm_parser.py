# -*- coding: utf-8 -*- 

"""
This class handles parsing of a single .vm file
"""

import os

if os.getcwd().endswith('VMTranslator'):
    from vm_translator import assembly_code as asm
    
else:
    import assembly_code as asm
    

class Parser:
    """
    Encapsulates access to input code. 
    
    Reads a VM command, parses it and provides convenient access
    to its components. In addition, removes all white space and comments. 
    """
    
    def __init__(self, fname):
        """
        Opens input file/stream and prepares to parse.
        """
        
        self._file_path = fname  
        with open(fname) as f:
            self._content = [line.strip() for line in f.readlines()]            
                  
        self._current_command = 0                
        self._next_command = 0
        self._current_args = []
        
        self._math_commands = list(asm.math_table.keys()) 
        self._command_type_table = {
            'pop': 'C_POP',
            'push': 'C_PUSH',            
            'label': 'C_LABEL',
            'goto': 'C_GOTO',
            'if-goto': 'C_IF',
            'function': 'C_FUNCTION',
            'call': 'C_CALL', 
            'return': 'C_RETURN'                  
        }
        self._command_types = list(self._command_type_table.keys()) 
   
    def __str__(self):        
        to_print =  '           Reading file: ' + self._file_path + '\n'
        to_print += '    Current line number: ' + str(self._current_command) + '\n'
        to_print += '           Current line: ' + self._content[self._current_command] + '\n'
        to_print += '      Next command line: ' + str(self._next_command) + '\n'
        to_print += '           Next command: ' + self._content[self._next_command] + '\n' 
        return to_print 
                
    def has_more_commands(self):
        """
        Checks to see if there are any more commands in input.
        Sets line index of next command, if there is one, and returns Boolean.  
        """
        
        #if current command has already run once, then increment by 1  
        start = 0
        if self._current_command:
            start = self._current_command + 1
        end = len(self._content) 
        
        for index in range(start, end):
            line = self._content[index]
            
            if not len(line) or line.replace(' ','').startswith('//'):
                continue
            
            elif line.split()[0] in self._math_commands + self._command_types:                
                self._next_command = index    
                return True 

            else:
                continue            

        return False       
    
    def advance(self):
        """
        Reads the next command from input, makes it the current command and runs parse_command(). 
        Should be called only if has_more_commands() is true. Initially there is no current command.
        """     
        
        self._current_command = self._next_command  
        self._parse_command()        
        return self._current_command   

    def _parse_command(self):
        """
        Parses command into its parts and saves it as a list to self._current_args 
        """
    
        self._current_args = self._content[self._current_command].split('//')[0].split()
    
    def command_type(self):
        """
        Returns type of current command:
        - C_ARITHMETIC
        - C_PUSH, C_POP
        - C_LABEL, C_GOTO
        - C_IF
        - C_FUNCTION
        - C_RETURN
        - C_CALL 
        
        C_ARITHMETIC is returned for all arithmetic VM commands.
        """ 
        
        command = self._current_args[0]
        
        #if command in ['add','sub','neg','eq','gt','lt','and','or','not']
        if command in self._math_commands:                
            return 'C_ARITHMETIC'
        
        elif command in self._command_type_table:
            return self._command_type_table[command]
            
        return None               
        
    def get_args(self):  
        """
        Returns current args as list.       
        """    
        
        return self._current_args  
        
    
    
    
    
    