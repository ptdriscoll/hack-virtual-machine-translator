// function Sys.init 0
(Sys.init)

// Sys.init: push constant 4000
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.init: pop pointer 0
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

// Sys.init: push constant 5000
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.init: pop pointer 1
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

// call Sys.main 0
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
@5
D=D-A
@ARG
M=D // ARG = SP-n-5

@SP
D=M
@LCL
M=D // LCL = SP

@Sys.main
0;JMP // goto f

(Sys.init$return.1)

// Sys.init: pop temp 1
@1
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

(Sys.init$LOOP)

@Sys.init$LOOP
0;JMP // goto

// function Sys.main 5
(Sys.main)

// Sys.main: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push constant 4001
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: pop pointer 0
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

// Sys.main: push constant 5001
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: pop pointer 1
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

// Sys.main: push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: pop local 1
@1
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

// Sys.main: push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: pop local 2
@2
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

// Sys.main: push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: pop local 3
@3
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

// Sys.main: push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Sys.add12 1
@Sys.main$return.1
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

@Sys.add12
0;JMP // goto f

(Sys.main$return.1)

// Sys.main: pop temp 0
@0
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

// Sys.main: push local 0
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

// Sys.main: push local 1
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

// Sys.main: push local 2
@2
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push local 3
@3
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: push local 4
@4
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// Sys.main: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// Sys.main: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// Sys.main: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// Sys.main: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// return from Sys.main
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

// function Sys.add12 0
(Sys.add12)

// Sys.add12: push constant 4002
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.add12: pop pointer 0
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

// Sys.add12: push constant 5002
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.add12: pop pointer 1
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

// Sys.add12: push argument 0
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

// Sys.add12: push constant 12
@12
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.add12: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// return from Sys.add12
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

