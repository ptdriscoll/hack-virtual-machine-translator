# -*- coding: utf-8 -*- 

"""
Tests code_writer write method. Runs from VMTranslator root directory.
To run tests in command line, i.e. for test_1_4 tests: prompt> python -m tests.test_1_4
To run a specific test, note addition of unittest: prompt> python -m unittest tests.test_1_4.CodeWriterBasic.test_constant
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import vm_translator 
from vm_translator import code_writer
import unittest
import shutil


class CodeWriterBasic(unittest.TestCase):
    """
    Check code_writer.write on BasicTest 
    """
    
    print('\nCHECKING BasicTest')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/BasicTest.asm')
        self.writer.set_file_name('BasicTest')
        with open('./data/BasicTest.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
      
    def test_constant(self):
        command, segment, index = self.lines[6].split() 
        self.writer.write('C_PUSH', [command, segment, index])
        self.writer.close()
        compare = '// BasicTest: push constant 10' + '''
                  @10
                  D=A
                  @SP
                  A=M
                  M=D
                  @SP
                  M=M+1
                  
                  '''.replace(' ','')       

        shutil.move('./data/BasicTest.asm', './data/BasicTest.txt')
        with open('./data/BasicTest.txt') as f:
            content = f.read()       
        self.assertEqual(content, compare) 
        
    def test_pop_local(self):
        command, segment, index = self.lines[7].split() 
        self.writer.write('C_POP', [command, segment, index])
        self.writer.close()
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

        shutil.move('./data/BasicTest.asm', './data/BasicTest.txt')
        with open('./data/BasicTest.txt') as f:
            content = f.read()       
        self.assertEqual(content, compare)
        
    def test_add(self):
        command = self.lines[22].split()[0] 
        self.writer.write('C_ARITHMETIC', [command])
        self.writer.close()
        compare = '// BasicTest: add' + '''
                  @SP
                  M=M-1
                  A=M
                  D=M
                  A=A-1
                  M=D+M
                  
                  '''.replace(' ','')
                  
        shutil.move('./data/BasicTest.asm', './data/BasicTest.txt')
        with open('./data/BasicTest.txt') as f:
            content = f.read()       
        self.assertEqual(content, compare)          
        
if __name__=='__main__':
    unittest.main()