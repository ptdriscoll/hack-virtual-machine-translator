# -*- coding: utf-8 -*- 

"""
Dictionaries and functions that map virtual-machine commands to assembly-code snippets. 
"""


symbol_table = {
    'local': 'LCL', 
    'constant': 'constant',
    'argument': 'ARG', 
    'this': 'THIS', 
    'that': 'THAT', 
    'temp': 'R5',
    'pointer': 'R3'
}

math_table = {
    'add': 'D+M',
    'sub': 'M-D',
    'neg': '-M',
    'eq': 'EQ',
    'gt': 'GT',
    'lt': 'LT',
    'and': '&',
    'or': '|',
    'not': '!'    
}

non_pointer_segments = ['R0','R1','R2','R3','R4','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','R15']

def pop_cmd(segment, index, static=False, note=''):
    """
    Accepts memory segment and memory segment index,
    and returns assembly code for pop command.
    """
    
    code = ''
    
    if static:
        code += '''@{segment}.{index}
        D=A    
        '''.format(segment=segment, index=index)
    
    else: 
        code += '''@{index}
        D=A
        @{segment}
        '''.format(index=index, segment=segment)
        
        if segment in non_pointer_segments:
            code += '''D=D+A
            '''  

        else:
            code += '''D=D+M
            '''         
        
    code += '''@R13
    M=D
    @SP
    M=M-1
    A=M
    D=M
    @R13
    A=M
    M=D'''    
    
    code = code.replace(' ','')    
    code += '{note}'.format(note=note) 
    if not note:
        code += '\n'
    
    return code
    
def push_cmd(segment, index, static=False, note=''):
    """
    Accepts memory segment and memory segment index,
    and returns assembly code for push command.    
    """
    
    code = ''''''
    
    if static:
        code += '''@{segment}.{index}
        D=M
        '''.format(segment=segment, index=index) 
    
    else:     
        code += '''@{index}
        D=A
        '''.format(index=index)
        
        if segment != 'constant':        
            code += '''@{segment}
            '''.format(segment=segment)  
            
            if segment in non_pointer_segments:
                code += '''A=D+A
                D=M
                '''        
    
            else:
                code += '''A=D+M
                D=M
                ''' 
    
    code += '''@SP
    A=M
    M=D
    @SP
    M=M+1'''
    
    code = code.replace(' ','')    
    code += '{note}'.format(note=note) 
    if not note:
        code += '\n' 

    return code

def math_cmd(command):
    """
    Accepts math command string and returns assembly code for math operation, 
    and returns assembly code:
    - command = D+M, M-D or -M
    - command string = add, sub or neg
    """
    
    if command == '-M':
        code = '''@SP
        A=M-1
        M=-M
        '''    
    else:
        code = '''@SP
        M=M-1
        A=M
        D=M
        A=A-1
        M={command}
        '''.format(command=command)
    
    return code.replace(' ','')    
    
def compare_cmd(command, jump):
    """
    Accepts two string arguments and returns assembly code for comparison operation, 
    and returns assembly code:
    - command = EQ, GT or LT
    - command string = eq, gt or lt
    - jump label includes incremented number each time a jump is used by CodeWriter instance    
    """
    
    code = '''@SP
    M=M-1
    A=M
    D=M
    A=A-1
    D=M-D
    M=-1
    @{jump}
    D;J{command}
    @SP
    A=M-1
    M=0
    ({jump})
    '''.format(command=command,   
               jump=jump)
               
    return code.replace(' ','')
    
def logic_cmd(command):
    """
    Accepts logic command string and returns assembly code for logical operation, 
    and returns assembly code:
    - command = &, |, !
    - command string = and, or, not 
    """
    
    if command == '!':
        code = '''@SP
        A=M-1
        M=!M
        '''    
    else:
        code = '''@SP
        M=M-1
        A=M
        D=M
        A=A-1
        M=D{command}M
        '''.format(command=command)
    
    return code.replace(' ','')  
    
def flow_cmd(command, label, note=''):
    """
    Accepts program flow command string and returns assembly code.
    Program flow commands can be: label, goto or if-goto     
    """
    
    if command == 'label':
        code = '({label})\n'.format(label=label)

    elif command == 'goto':
        code = '@{label}\n'.format(label=label)  
        
        #if label points to a temp variable, make it a pointer
        if label in ['R13','R14','R15']:
            code += 'A=M\n'
        
        code += '0;JMP{note}\n'.format(note=note)  

    elif command == 'if-goto': 
        code = '''@SP
        M=M-1
        A=M
        D=M
        '''        
        
        code = code.replace(' ','')        
        code += '@{label}\n'.format(label=label) 
        code += 'D;JNE{note}\n'.format(note=note)          
    
    return code 
    
def assign_cmd(save_to, save_from, frame_steps=None, note=''):
    """
    Assigns value from one RAM location to another.
    Frame_steps are number of negative or positive steps away from save_from      
    """
    
    code = '''@{save_from}
    D=M
    '''.format(save_from=save_from)
    
    if frame_steps:
        if frame_steps < 0:
            plus_or_minus = '-'
            frame_steps = abs(frame_steps)
        else:
            plus_or_minus = '+'  
            
        frame_steps = str(frame_steps)   

        code += '''@{frame_steps}
        D=D{plus_or_minus}A
        '''.format(frame_steps=frame_steps, plus_or_minus=plus_or_minus)             
    
    code += '''@{save_to}
    M=D'''.format(save_to=save_to)    
    
    code = code.replace(' ','')     
    code += '{note}'.format(note=note)       
    
    return code    
    
def assign_pointer_cmd(save_to, save_from, frame_steps=None, note=''):
    """
    Assigns value from pointer to RAM location to another RAM location.
    Frame_steps are number of negative or positive steps away from save_from     
    """
    
    code = '@{save_from}\n'.format(save_from=save_from)
    
    if frame_steps:
        if frame_steps < 0:
            plus_or_minus = '-'
            frame_steps = abs(frame_steps)
        else:
            plus_or_minus = '+'  
            
        frame_steps = str(frame_steps)
        
        code += '''D=M
        @{frame_steps}
        A=D{plus_or_minus}A
        D=M
        '''.format(frame_steps=frame_steps, plus_or_minus=plus_or_minus) 
        
    else:
        code += '''
        A=M
        D=M
        '''            
    
    code += '''@{save_to}
    M=D'''.format(save_to=save_to) 
    
    code = code.replace(' ','')     
    code += '{note}'.format(note=note)       
    
    return code     
    
def assign_value_cmd(save_to, save_from, note=''):    
    """
    Assigns value to RAM location.   
    """    
    code = '''@{save_from}
    D=A
    @{save_to}
    M=D
    '''.format(save_from=save_from, save_to=save_to)            
   
    code = code.replace(' ','')     
    code += '{note}'.format(note=note)       
    
    return code     