# Assembler
Hack Machine Langue Translator Using Python

@Execute Instruction: in Window OS

- Compile: Type "filename"(end with py) in ternminal, then hit enter.
"filename": Code.py; SymbolTable.py; Parser.py ; Assembler.py

- For being tested and running the translator, just type:
	Assembler.py "filepath"
The assembler will translate the filename.asm into filename.hack
- If the test file and assembler in the same folder,  we can type:
	Assembler.py filename
	Example: Assembler.py rect.asm -> output will be rect.hack
	
- Example: running this in ternminal:
	Assembler.py "C:\Users\Desktop\nand2tetris\projects\06\rect\Rect.asm"
That will translate the rect.asm in project 06 of nand2tetris folder and output file
rect.hack in the same directory. This line will appear in the ternminal:
	Translating C:\Users\Desktop\nand2tetris\projects\06\rect\Rect.asm
	
@Project Description

##	My Assembler for the Hack language implemented in Python 3.
##	So with any computer that capable of running python file should be ok.
	My code has 4 classes, which are:
- Assembler
	+ Ensuring that 2 passes are made when translate .asm file into .hack
	+ Handle file input/output.
	+ Takt .asm file and output .hack
	+ Include all 3 other classes.
	+ Worked, compiled successfully.
	
- Code
	+ Translate the hack assembly language mnemonics into binary code
	+ Worked, compiled successfully
	
- Parser: 
	+ Encapsulates access to the input code. Reads an assembly language
    command, parses it, and provides convenient access to the command's
    components (fields/symbols). Removes all whitespace and comments
	+ Worked, compiled successfully
	
- SymbolTable
	+ Keep the correspondence between symbolic label and number addresses
	+ Have create empty table with predefined addresses for R0..R15 and
	Screen and KBD; Add pair input to table, chekc if the table contain
	given symbols and return associated addresses.
	+ Worked, compiled successfully
 
@Testing/Debugging
- I have fixed all the bugs I could find during implementing and testing
+ Fixing issue when Parser not removing all whitespaces.
+ Spiltting the assembly into 2 passes.
+ Fixing missing entry in the jump translate.

- Testing:
+ Running through all.asm provided in the project 06 of nand2tetris
+ Comparing .hack file output in Window terminal by: 
fc /b file1 file2
+ All cases tested successfully
