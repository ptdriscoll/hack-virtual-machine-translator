// BasicLoop: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicLoop: pop local 0
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

(BasicLoop$LOOP_START)

// BasicLoop: push argument 0
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

// BasicLoop: push local 0
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

// BasicLoop: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// BasicLoop: pop local 0
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

// BasicLoop: push argument 0
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

// BasicLoop: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// BasicLoop: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// BasicLoop: pop argument 0
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
M=D

// BasicLoop: push argument 0
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

@SP
M=M-1
A=M
D=M
@BasicLoop$LOOP_START
D;JNE // if-goto

// BasicLoop: push local 0
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

