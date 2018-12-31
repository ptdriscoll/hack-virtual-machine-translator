// Initialize stack pointer to 256
@256
D=A
@SP
M=D

// call Sys.init 0
@Sys$return.1
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
@5
D=D-A
@ARG
M=D // ARG = SP-n-5

@SP
D=M
@LCL
M=D // LCL = SP

@Sys.init
0;JMP // goto f

(Sys$return.1)

// function Main.fibonacci 0
(Main.fibonacci)

// Main.fibonacci: push argument 0
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

// Main.fibonacci: push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// Main.fibonacci: lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@Main.fibonacci$JUMP.1
D;JLT
@SP
A=M-1
M=0
(Main.fibonacci$JUMP.1)

@SP
M=M-1
A=M
D=M
@Main.fibonacci$IF_TRUE
D;JNE // if-goto

@Main.fibonacci$IF_FALSE
0;JMP // goto

(Main.fibonacci$IF_TRUE)

// Main.fibonacci: push argument 0
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

// return from Main.fibonacci
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

(Main.fibonacci$IF_FALSE)

// Main.fibonacci: push argument 0
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

// Main.fibonacci: push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1

// Main.fibonacci: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// call Main.fibonacci 1
@Main.fibonacci$return.1
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

(Main.fibonacci$return.1)

// Main.fibonacci: push argument 0
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

// Main.fibonacci: push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1

// Main.fibonacci: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// call Main.fibonacci 1
@Main.fibonacci$return.2
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

(Main.fibonacci$return.2)

// Main.fibonacci: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// return from Main.fibonacci
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

