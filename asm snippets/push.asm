// addr = LCL+3, *SP=*addr, SP++
// variables are LCL and 3

// D = addr = LCL+3
@3  
D=A
@LCL
A=D+M
D=M

// *SP=*addr
@SP 
A=M
M=D

// SP++
@SP 
M=M+1