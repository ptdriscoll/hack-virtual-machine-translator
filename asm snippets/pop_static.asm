// addr = fname.2, SP--, *addr=*SP
// variables are fname.2

// R13 = addr = fname.2
@fname.2
D=A
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