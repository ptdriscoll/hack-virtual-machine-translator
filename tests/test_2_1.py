# -*- coding: utf-8 -*- 

"""
Tests label and jump commands. Runs from VMTranslator root directory.
To run tests in command line, i.e. for test_2_1 tests: prompt> python -m tests.test_2_1
To run a specific test, note addition of unittest: prompt> python -m unittest tests.test_2_1.Label.test_label
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import vm_translator 
from vm_translator import code_writer
import unittest


class Label(unittest.TestCase):
    """
    Check write labels
    """
    
    print('\nCHECKING Label')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/BasicLoop.asm')
        self.writer.set_file_name('BasicLoop')
        with open('./data/BasicLoop.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()  
        
    #def test_init(self):
    #    print()
    #    print(self.writer)      

    def test_label(self):
        command, label = self.lines[10].split('//')[0].split() 
        result = self.writer.write_flow(command, label)        
        compare = '(BasicLoop$LOOP_START)\n\n'
        self.assertEqual(compare, result)
        
        result = self.writer.write('C_LABEL', [command, label])
        self.assertEqual(compare, result)
        
class Goto(unittest.TestCase):
    """
    Check write goto and if-goto
    """
    
    print('\nCHECKING Goto and If-goto')
    
    def setUp(self):
        self.writer = code_writer.CodeWriter('./data/FibonacciSeries.asm')
        self.writer.set_file_name('FibonacciSeries')
        with open('./data/FibonacciSeries.vm') as f:
            self.lines = [line.strip() for line in f.readlines()]
            
    def tearDown(self):    
        self.writer.close()  
        
    #def test_init(self):
    #    print()
    #    print(self.writer)      

    def test_goto(self):
        command, label = self.lines[27].split('//')[0].split() 
        result = self.writer.write_flow(command, label)        
        compare = '@FibonacciSeries$END_PROGRAM\n'
        compare += '0;JMP // goto\n\n'                  
        self.assertEqual(compare, result)
        
        result = self.writer.write('C_GOTO', [command, label])
        self.assertEqual(compare, result)
        
    def test_if_goto(self):
        command, label = self.lines[26].split('//')[0].split() 
        result = self.writer.write_flow(command, label)        
        compare = '''@SP
                  M=M-1
                  A=M
                  D=M
                  @FibonacciSeries$COMPUTE_ELEMENT
                  '''.replace(' ','')
        compare += 'D;JNE // if-goto\n\n'
        self.assertEqual(compare, result)
        
        result = self.writer.write('C_IF', [command, label])
        self.assertEqual(compare, result)
        
if __name__=='__main__':
    unittest.main()