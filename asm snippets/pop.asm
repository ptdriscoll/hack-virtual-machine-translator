// addr = LCL+3, SP--, *addr=*SP
// variables are LCL and 3

// R13 = addr = LCL+3
@3  
D=A
@LCL
D=D+M
@R13
M=D

// SP--
@SP
M=M-1

// *addr=*SP 
A=M
D=M
@R13
A=M
M=D