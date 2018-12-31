# -*- coding: utf-8 -*- 

"""
Tests 9 stack arithmetic and logical commands. Runs from VMTranslator root directory.
To run tests in command line, i.e. for test_1_2 tests: prompt> python -m tests.test_1_2
To run a specific test, note addition of unittest: prompt> python -m unittest tests.test_1_2.CodeWriterBasic.test_add
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import vm_translator 
from vm_translator import code_writer
import unittest


class CodeWriterBasic(unittest.TestCase):
    """
    Check write_arithmetic on BasicTest 
    """
    
    print('\nCHECKING BasicTest')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/BasicTest.asm')
        self.writer.set_file_name('BasicTest')
        with open('./data/BasicTest.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()             
       
    def test_add(self):
        command = self.lines[22].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// BasicTest: add' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  M=D+M
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)        
        
    def test_sub(self):
        command = self.lines[24].split()[0] 
        #print(command)
        result = self.writer.write_arithmetic(command)
        compare = '// BasicTest: sub' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  M=M-D
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)         
        
class CodeWriterStack(unittest.TestCase):
    """
    Check write_arithmetic on StackTest
    """
    
    print('\nCHECKING StackTest')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/StackTest.asm')
        self.writer.set_file_name('StackTest')
        with open('./data/StackTest.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()             
            
    def test_neg(self):
        command = self.lines[40].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: neg' + '''
                  @SP
                  A=M-1
                  M=-M
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)                
       
    def test_compare(self):
        command = self.lines[9].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: eq' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  D=M-D
                  M=-1
                  @StackTest$JUMP.1
                  D;JEQ
                  @SP
                  A=M-1
                  M=0
                  (StackTest$JUMP.1)
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)       

        command = self.lines[18].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: lt' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  D=M-D
                  M=-1
                  @StackTest$JUMP.2
                  D;JLT
                  @SP
                  A=M-1
                  M=0
                  (StackTest$JUMP.2)
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line) 
            
        command = self.lines[27].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: gt' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  D=M-D
                  M=-1
                  @StackTest$JUMP.3
                  D;JGT
                  @SP
                  A=M-1
                  M=0
                  (StackTest$JUMP.3)
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)          

    def test_and(self):
        command = self.lines[41].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: and' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  M=D&M
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)  
       
    def test_and(self):
        command = self.lines[43].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: or' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  M=D|M
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)          
    
    def test_or(self):
        command = self.lines[44].split()[0] 
        result = self.writer.write_arithmetic(command)
        compare = '// StackTest: not' + '''
                  @SP
                  A=M-1
                  M=!M
                  
                  '''.replace(' ','')
        self.assertEqual(compare, result)
        #print()
        #for line in result.split('\n'):
        #    print(line)          
        
if __name__=='__main__':
    unittest.main()