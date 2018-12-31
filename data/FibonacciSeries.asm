// FibonacciSeries: push argument 1
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

// FibonacciSeries: pop pointer 1
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

// FibonacciSeries: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: pop that 0
@0
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

// FibonacciSeries: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: pop that 1
@1
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

// FibonacciSeries: push argument 0
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

// FibonacciSeries: push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// FibonacciSeries: pop argument 0
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

(FibonacciSeries$MAIN_LOOP_START)

// FibonacciSeries: push argument 0
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
@FibonacciSeries$COMPUTE_ELEMENT
D;JNE // if-goto

@FibonacciSeries$END_PROGRAM
0;JMP // goto

(FibonacciSeries$COMPUTE_ELEMENT)

// FibonacciSeries: push that 0
@0
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: push that 1
@1
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// FibonacciSeries: pop that 2
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

// FibonacciSeries: push pointer 1
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

// FibonacciSeries: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// FibonacciSeries: pop pointer 1
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

// FibonacciSeries: push argument 0
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

// FibonacciSeries: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// FibonacciSeries: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// FibonacciSeries: pop argument 0
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

@FibonacciSeries$MAIN_LOOP_START
0;JMP // goto

(FibonacciSeries$END_PROGRAM)

