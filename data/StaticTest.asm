// StaticTest: push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1

// StaticTest: push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1

// StaticTest: push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1

// StaticTest: pop static 8
@StaticTest.8
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// StaticTest: pop static 3
@StaticTest.3
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// StaticTest: pop static 1
@StaticTest.1
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// StaticTest: push static 3
@StaticTest.3
D=M
@SP
A=M
M=D
@SP
M=M+1

// StaticTest: push static 1
@StaticTest.1
D=M
@SP
A=M
M=D
@SP
M=M+1

// StaticTest: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// StaticTest: push static 8
@StaticTest.8
D=M
@SP
A=M
M=D
@SP
M=M+1

// StaticTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

