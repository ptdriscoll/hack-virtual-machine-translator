// BasicTest: push constant 10
@10
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: pop local 0
@0
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// BasicTest: push constant 21
@21
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: push constant 22
@22
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: pop argument 2
@2
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
M=D

// BasicTest: pop argument 1
@1
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
M=D

// BasicTest: push constant 36
@36
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: pop this 6
@6
D=A
@THIS
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// BasicTest: push constant 42
@42
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: push constant 45
@45
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: pop that 5
@5
D=A
@THAT
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// BasicTest: pop that 2
@2
D=A
@THAT
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// BasicTest: push constant 510
@510
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: pop temp 6
@6
D=A
@R5
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D

// BasicTest: push local 0
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

// BasicTest: push that 5
@5
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// BasicTest: push argument 1
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

// BasicTest: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// BasicTest: push this 6
@6
D=A
@THIS
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: push this 6
@6
D=A
@THIS
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// BasicTest: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// BasicTest: push temp 6
@6
D=A
@R5
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// BasicTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

