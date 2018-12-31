# -*- coding: utf-8 -*- 

"""
Tests Parser. Runs from VMTranslator root directory.
To run tests in command line, i.e. for test_1_3 tests: prompt> python -m tests.test_1_3
To run a specific test, note addition of unittest: prompt> python -m unittest tests.test_1_3.ParserBasic.test_init
To run all tests in the tests package: prompt> python -m unittest
"""

from .context import vm_translator 
from vm_translator import vm_parser
import unittest


class ParserBasic(unittest.TestCase):
    """
    Check write_arithmetic on BasicTest 
    """
    
    print('\nCHECKING BasicTest')
    
    def setUp(self):
        self.parser = vm_parser.Parser('./data/BasicTest.vm')
       
    def test_init(self):
        #print(self.parser)
        more_commands = self.parser.has_more_commands()
        #print(self.parser)
        self.assertTrue(more_commands)  
        
        current_command = self.parser.advance()
        #print(self.parser)      
        self.assertEqual(current_command, 6)
        self.assertEqual(self.parser.command_type(), 'C_PUSH')
        self.assertEqual(self.parser.get_args()[1], 'constant') 
        self.assertEqual(self.parser.get_args()[2], '10')         
        
        self.parser.has_more_commands()
        current_command = self.parser.advance()
        #print(self.parser)      
        self.assertEqual(current_command, 7)
        self.assertEqual(self.parser.command_type(), 'C_POP')
        self.assertEqual(self.parser.get_args()[1], 'local') 
        self.assertEqual(self.parser.get_args()[2], '0')         
        
        for x in range(14):
            self.parser.has_more_commands() 
            self.parser.advance()         

        self.parser.has_more_commands()
        current_command = self.parser.advance()    
        #print(self.parser)      
        self.assertEqual(current_command, 22)
        self.assertEqual(self.parser.command_type(), 'C_ARITHMETIC')
        self.assertEqual(self.parser.get_args()[0], 'add')
        
        self.parser.has_more_commands()
        current_command = self.parser.advance()    
        #print(self.parser)      
        self.assertEqual(current_command, 23)
        self.assertEqual(self.parser.command_type(), 'C_PUSH')
        self.assertEqual(self.parser.get_args()[1], 'argument') 
        self.assertEqual(self.parser.get_args()[2], '1')          
        
        self.parser.has_more_commands()
        current_command = self.parser.advance()    
        #print(self.parser)      
        self.assertEqual(current_command, 24)
        self.assertEqual(self.parser.command_type(), 'C_ARITHMETIC')
        self.assertEqual(self.parser.get_args()[0], 'sub') 
        
if __name__=='__main__':
    unittest.main()