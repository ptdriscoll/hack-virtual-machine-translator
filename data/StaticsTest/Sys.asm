// function Sys.init 0
(Sys.init)

// Sys.init: push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.init: push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class1.set 2
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
@7
D=D-A
@ARG
M=D // ARG = SP-n-5

@SP
D=M
@LCL
M=D // LCL = SP

@Class1.set
0;JMP // goto f

(Sys.init$return.1)

// Sys.init: pop temp 0
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

// Sys.init: push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// Sys.init: push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class2.set 2
@Sys.init$return.2
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
@7
D=D-A
@ARG
M=D // ARG = SP-n-5

@SP
D=M
@LCL
M=D // LCL = SP

@Class2.set
0;JMP // goto f

(Sys.init$return.2)

// Sys.init: pop temp 0
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

// call Class1.get 0
@Sys.init$return.3
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

@Class1.get
0;JMP // goto f

(Sys.init$return.3)

// call Class2.get 0
@Sys.init$return.4
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

@Class2.get
0;JMP // goto f

(Sys.init$return.4)

(Sys.init$WHILE)

@Sys.init$WHILE
0;JMP // goto

