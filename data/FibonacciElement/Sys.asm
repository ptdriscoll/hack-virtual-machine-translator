// function Sys.init 0
(Sys.init)

// Sys.init: push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Main.fibonacci 1
@Sys.init$return.1
D=A
@SP
A=M
M=D
@SP
M=M+1 // push return-address

@0
D=A
@R1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1 // push LCL

@0
D=A
@R2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1 // push ARG

@0
D=A
@R3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1 // push THIS

@0
D=A
@R4
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1 // push THAT

@SP
D=M
@6
D=D-A
@ARG
M=D // ARG = SP-n-5

@SP
D=M
@LCL
M=D // LCL = SP

@Main.fibonacci
0;JMP // goto f

(Sys.init$return.1)

(Sys.init$WHILE)

@Sys.init$WHILE
0;JMP // goto

