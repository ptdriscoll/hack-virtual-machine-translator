# -*- coding: utf-8 -*- 

"""
Tests function declarations, calls and returns. Runs from VMTranslator root directory.
To run tests in command line, i.e. for test_2_2 tests: prompt> python -m tests.test_2_2
To run a specific test, note addition of unittest: prompt> python -m unittest tests.test_2_2.Functions.test_label
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import vm_translator 
from vm_translator import code_writer
import unittest


class Functions(unittest.TestCase):
    """
    Check declare and return function
    """
    
    print('\nCHECKING Function label and return')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/SimpleFunction.asm')
        self.writer.set_file_name('SimpleFunction')
        with open('./data/SimpleFunction.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()  
        
    #def test_init(self):
    #    print()
    #    print(self.writer)      

    def test_label(self):
        command, fname, nlocals = self.lines[6].split('//')[0].split() 
        #result = self.writer.write_function(command, fname, nlocals)
        result = self.writer.write('C_FUNCTION', [command, fname, nlocals])
        
        compare = '// function SimpleFunction.test 2\n'
        compare += '(SimpleFunction.test)\n\n'
        compare += '// SimpleFunction.test: push constant 0' + '''
                  @0
                  D=A
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')
                  
        compare += '// SimpleFunction.test: push constant 0' + '''
                  @0
                  D=A
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')  
        
        self.assertEqual(compare, result)        
        
    def test_return(self):
        self.writer.set_function_name('SimpleFunction.test')
        command = self.lines[15].split('//')[0].split()[0] 
        result = self.writer.write_return(command) 
        #result = self.writer.write('C_RETURN', [command])  
        compare = '// return from SimpleFunction.test\n'        
        compare +=  '''@LCL
                   D=M
                   @R14
                   M=D'''.replace(' ','')
        compare += ' // endFrame = LCL\n\n'           
                   
        compare += '''@R14
                   D=M
                   @5
                   A=D-A
                   D=M
                   @R15
                   M=D'''.replace(' ','')
        compare += ' // retAddr = *(endFrame-5)\n\n'                    

        compare += '''@0
                   D=A
                   @ARG
                   D=D+M
                   @R13
                   M=D
                   @SP
                   M=M-1
                   A=M
                   D=M
                   @R13
                   A=M
                   M=D'''.replace(' ','')
        compare += ' // *ARG = pop()\n\n'                    

        compare += '''@ARG
                   D=M
                   @1
                   D=D+A
                   @SP
                   M=D'''.replace(' ','')
        compare += ' // SP = ARG+1\n\n'                    

        compare += '''@R14
                   D=M
                   @1
                   A=D-A
                   D=M
                   @THAT
                   M=D'''.replace(' ','')
        compare += ' // THAT = *(endFrame-1)\n\n'                    

        compare += '''@R14
                   D=M
                   @2
                   A=D-A
                   D=M
                   @THIS
                   M=D'''.replace(' ','')
        compare += ' // THIS = *(endFrame-2)\n\n'                    

        compare += '''@R14
                   D=M
                   @3
                   A=D-A
                   D=M
                   @ARG
                   M=D'''.replace(' ','')
        compare += ' // ARG = *(endFrame-3)\n\n'                    

        compare += '''@R14
                   D=M
                   @4
                   A=D-A
                   D=M
                   @LCL
                   M=D'''.replace(' ','')
        compare += ' // LCL = *(endFrame-4)\n\n'                    

        compare += '''@R15
                   A=M
                   0;JMP'''.replace(' ','')
        compare += ' // goto retAddr\n\n'                    
        
        self.assertEqual(compare, result)

class Fibonacci(unittest.TestCase):
    """
    Check call function
    """
    
    print('\nCHECKING Function call')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/FibonacciElement/Main.asm')
        self.writer.set_file_name('Main')
        with open('./data/FibonacciElement/Main.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()  
        
    #def test_init(self):
    #    print()
    #    print(self.writer)      

    def test_label(self):
        command, fname, nargs = self.lines[23].split('//')[0].split() 
        #result = self.writer.write_function(command, fname, nargs)
        result = self.writer.write('C_CALL', [command, fname, nargs])        
        compare = '// call Main.fibonacci 1\n'
        compare += '''@Main$return.1
                   D=A
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1'''.replace(' ','')
        compare += ' // push return-address\n\n'

        compare += '''@0
                   D=A
                   @R1
                   A=D+A
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1'''.replace(' ','')
        compare += ' // push LCL\n\n'

        compare += '''@0
                   D=A
                   @R2
                   A=D+A
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1'''.replace(' ','')
        compare += ' // push ARG\n\n'

        compare += '''@0
                   D=A
                   @R3
                   A=D+A
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1'''.replace(' ','')
        compare += ' // push THIS\n\n'

        compare += '''@0
                   D=A
                   @R4
                   A=D+A
                   D=M
                   @SP
                   A=M
                   M=D
                   @SP
                   M=M+1'''.replace(' ','')
        compare += ' // push THAT\n\n'

        compare += '''@SP
                   D=M
                   @6
                   D=D-A
                   @ARG
                   M=D'''.replace(' ','')
        compare += ' // ARG = SP-n-5\n\n'

        compare += '''@SP
                   D=M
                   @LCL
                   M=D'''.replace(' ','')
        compare += ' // LCL = SP\n\n'

        compare += '@Main.fibonacci\n'
        compare += '0;JMP // goto f\n\n'
        compare += '(Main$return.1)\n\n'
        
        self.assertEqual(compare, result)         
        
if __name__=='__main__':
    unittest.main()