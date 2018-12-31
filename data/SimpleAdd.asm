// SimpleAdd: push constant 7
@7
D=A
@SP
A=M
M=D
@SP
M=M+1

// SimpleAdd: push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// SimpleAdd: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

