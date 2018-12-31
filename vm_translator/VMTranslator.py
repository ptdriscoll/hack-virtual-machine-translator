# -*- coding: utf-8 -*- 

"""
The VM Translator accepts a single command line parameter, Xxx or Xxx.vm, where either 
Xxx is a directory containing one more .vm files, or Xxx.vm is a file containing VM code.

FROM vm_translator DIRECTORY:
-prompt> python VMTranslator.py Xxx
-prompt> python VMTranslator.py Xxx.vm
-prompt> python VMTranslator.py run_all

FROM VMTranslator DIRECTORY one level up:
-prompt> python -m vm_translator Xxx
-prompt> python -m vm_translator Xxx.vm
-prompt> python -m vm_translator run_all

The translator then translates the Xxx.vm file, or in case of a directory all .vm files. The result
is always a single assembly-language file named Xxx.asm. 
"""

import os, sys, ntpath 

if os.getcwd().endswith('VMTranslator'):
    from vm_translator import vm_parser
    from vm_translator import code_writer
    
else:
    import vm_parser
    import code_writer
    

def translate_file(file, file_full_path, writer):
    """
    Accepts name of virtual machine code file.
    Returns translation into assembly code, as a string. 
    """
    
    fname = file.replace('.vm', '')
    writer.set_file_name(fname)
    file_parser = vm_parser.Parser(file_full_path)
    
    while file_parser.has_more_commands():
        file_parser.advance()
        command_type = file_parser.command_type()
        args = file_parser.get_args()
        writer.write(command_type, args)
 
def translate(arg):
    """
    Checks command argument to see if its a directory of virtual machine code files or just one file.
    Writes translated assembly code to one file, whether working with a directory of vm files or just one file.
    The translated file, with an .asm extension, is saved to the same directory where the vm file/s reside.
    """

    #get directory or file from arg and, if on Windows, convert to back slashes
    print('\nUser input: \n\t' + arg)
    to_translate = arg.strip()  
    to_translate = os.path.abspath(to_translate) 
    
    #add trailing slash to last directory if it's missing
    #so to_write file can be appended
    if not to_translate.endswith('.vm'):
        to_translate = os.path.join(to_translate, '')   
    
    #get name to write to name.asm, using either name.vm or name directory 
    path, tail = ntpath.split(to_translate)    
    fname = tail or ntpath.basename(path)
    
    to_write = os.path.join(path, fname.replace('.vm', '') + '.asm')      
    writer = code_writer.CodeWriter(to_write)
    
    if os.path.isdir(to_translate):
        print('\nTranslating .vm files in directory: \n\t' + to_translate)
        print('\nTranslating to: \n\t' + to_write) 
        
        writer.write_init() #init asm code is added for directories only 
        
        for root, dirs, files in os.walk(to_translate):
            for file in files:
                if file.endswith('.vm'):
                    file_full_path = os.path.join(root, file)
                    translate_file(file, file_full_path, writer)
        
    else:
        print('\nTranslating file: \n\t' + to_translate)
        print('\nTranslating to: \n\t' + to_write) 
        translate_file(fname, to_translate, writer)
    
    writer.close()
    print('\nTranslation completed')  
    print('\n----------------------------------------------------------------------')    
    
def main():
    """
    Checks whether arg is run_all, or a file or directory.
    If run_all, then walks through data directory to translate all .vm files and directories.    
    """
    
    if sys.argv[1] == 'run_all':
        if os.getcwd().endswith('VMTranslator'):
            start_directory = 'data/'
        else:
            start_directory = '../data/'   
            
        for root, dirs, files in os.walk(start_directory):
            for file in files:
                if file.endswith('.vm'):
                    fname = os.path.join(root, file)
                    translate(fname)                    
            for dir in dirs:
                dname = os.path.join(root, dir)
                translate(dname)                     
        
    else:
        translate(sys.argv[1])
    
if __name__ == '__main__':
    main()   