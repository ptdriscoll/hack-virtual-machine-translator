// addr = fname.1, *SP=*addr, SP++
// variables are fname.1

// D = addr = fname.1
@fname.1
D=M

// *SP=*addr
@SP 
A=M
M=D

// SP++
@SP 
M=M+1