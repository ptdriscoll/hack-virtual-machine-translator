// PointerTest: push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: pop pointer 0
@0
D=A
@R3
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

// PointerTest: push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: pop pointer 1
@1
D=A
@R3
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

// PointerTest: push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: pop this 2
@2
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

// PointerTest: push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: pop that 6
@6
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

// PointerTest: push pointer 0
@0
D=A
@R3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: push pointer 1
@1
D=A
@R3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// PointerTest: push this 2
@2
D=A
@THIS
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// PointerTest: push that 6
@6
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// PointerTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

