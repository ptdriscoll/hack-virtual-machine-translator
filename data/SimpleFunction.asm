// function SimpleFunction.test 2
(SimpleFunction.test)

// SimpleFunction.test: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// SimpleFunction.test: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// SimpleFunction.test: push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// SimpleFunction.test: push local 1
@1
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// SimpleFunction.test: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// SimpleFunction.test: not
@SP
A=M-1
M=!M

// SimpleFunction.test: push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// SimpleFunction.test: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// SimpleFunction.test: push argument 1
@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// SimpleFunction.test: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// return from SimpleFunction.test
@LCL
D=M
@R14
M=D // endFrame = LCL

@R14
D=M
@5
A=D-A
D=M
@R15
M=D // retAddr = *(endFrame-5)

@0
D=A
@ARG
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D // *ARG = pop()

@ARG
D=M
@1
D=D+A
@SP
M=D // SP = ARG+1

@R14
D=M
@1
A=D-A
D=M
@THAT
M=D // THAT = *(endFrame-1)

@R14
D=M
@2
A=D-A
D=M
@THIS
M=D // THIS = *(endFrame-2)

@R14
D=M
@3
A=D-A
D=M
@ARG
M=D // ARG = *(endFrame-3)

@R14
D=M
@4
A=D-A
D=M
@LCL
M=D // LCL = *(endFrame-4)

@R15
A=M
0;JMP // goto retAddr

