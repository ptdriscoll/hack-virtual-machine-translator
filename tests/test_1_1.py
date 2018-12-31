# -*- coding: utf-8 -*- 

"""
Tests push and pop commands. Runs from VMTranslator root directory.
To run tests in command line, i.e. for test_1_1 tests: prompt> python -m tests.test_1_1
To run a specific test, note addition of unittest: prompt> python -m unittest tests.test_1_1.CodeWriterBasic.test_constant
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import vm_translator 
from vm_translator import code_writer
import unittest


class CodeWriterBasic(unittest.TestCase):
    """
    Check write_push_pop on BasicTest
    """
    
    print('\nCHECKING BasicTest')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/BasicTest.asm')
        self.writer.set_file_name('BasicTest')
        with open('./data/BasicTest.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()  
        
    #def test_init(self):
    #    print()
    #    print(self.writer)      

    def test_constant(self):
        command, segment, index = self.lines[6].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// BasicTest: push constant 10' + '''
                  @10
                  D=A
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)
      
    def test_pop_local(self):
        command, segment, index = self.lines[7].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// BasicTest: pop local 0' + '''
                  @0  
                  D=A
                  @LCL
                  D=D+M
                  @R13
                  M=D
                  @SP
                  M=M-1
                  A=M
                  D=M
                  @R13
                  A=M
                  M=D
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)         
        
    def test_pop_argument(self):
        command, segment, index = self.lines[10].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// BasicTest: pop argument 2' + '''
                  @2  
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
                  M=D
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)   
            
    def test_push_local(self):
        command, segment, index = self.lines[20].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// BasicTest: push local 0' + '''
                  @0  
                  D=A
                  @LCL
                  A=D+M
                  D=M
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)
        
    def test_pop_temp(self):
        command, segment, index = self.lines[19].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// BasicTest: pop temp 6' + '''
                  @6  
                  D=A
                  @R5
                  D=D+A
                  @R13
                  M=D
                  @SP
                  M=M-1
                  A=M
                  D=M
                  @R13
                  A=M
                  M=D
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)  

    def test_push_temp(self):
        command, segment, index = self.lines[29].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// BasicTest: push temp 6' + '''
                  @6  
                  D=A
                  @R5
                  A=D+A
                  D=M
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)          
        
class CodeWriterPointer(unittest.TestCase):
    """
    Check write_push_pop on PointerTest
    """
    
    print('\nCHECKING PointerTest')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/PointerTest.asm')
        self.writer.set_file_name('PointerTest')
        with open('./data/PointerTest.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()              
       
    def test_pop_pointer(self):
        command, segment, index = self.lines[8].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// PointerTest: pop pointer 0' + '''
                  @0  
                  D=A
                  @R3
                  D=D+A
                  @R13
                  M=D
                  @SP
                  M=M-1
                  A=M
                  D=M
                  @R13
                  A=M
                  M=D
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)   

    def test_push_pointer(self):
        command, segment, index = self.lines[16].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// PointerTest: push pointer 1' + '''
                  @1  
                  D=A
                  @R3
                  A=D+A
                  D=M
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)         
        
class CodeWriterStatic(unittest.TestCase):
    """
    Check write_push_pop on StaticTest
    """
    
    print('\nCHECKING StaticTest')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/StaticTest.asm')
        self.writer.set_file_name('StaticTest')
        with open('./data/StaticTest.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()              
       
    def test_pop_static(self):
        command, segment, index = self.lines[9].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// StaticTest: pop static 8' + '''
                  @StaticTest.8
                  D=A
                  @R13
                  M=D
                  @SP
                  M=M-1
                  A=M
                  D=M
                  @R13
                  A=M
                  M=D
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)      
        
    def test_push_static(self):
        command, segment, index = self.lines[12].split() 
        result = self.writer.write_push_pop(command, segment, index)
        compare = '// StaticTest: push static 3' + '''
                  @StaticTest.3
                  D=M
                  @SP
                  A=M
                  M=D
                  @SP 
                  M=M+1
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)
        
if __name__=='__main__':
    unittest.main()