// StackTest: push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.1
D;JEQ
@SP
A=M-1
M=0
(StackTest$JUMP.1)

// StackTest: push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.2
D;JEQ
@SP
A=M-1
M=0
(StackTest$JUMP.2)

// StackTest: push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: eq
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.3
D;JEQ
@SP
A=M-1
M=0
(StackTest$JUMP.3)

// StackTest: push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.4
D;JLT
@SP
A=M-1
M=0
(StackTest$JUMP.4)

// StackTest: push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.5
D;JLT
@SP
A=M-1
M=0
(StackTest$JUMP.5)

// StackTest: push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: lt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.6
D;JLT
@SP
A=M-1
M=0
(StackTest$JUMP.6)

// StackTest: push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.7
D;JGT
@SP
A=M-1
M=0
(StackTest$JUMP.7)

// StackTest: push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.8
D;JGT
@SP
A=M-1
M=0
(StackTest$JUMP.8)

// StackTest: push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: gt
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
M=-1
@StackTest$JUMP.9
D;JGT
@SP
A=M-1
M=0
(StackTest$JUMP.9)

// StackTest: push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M

// StackTest: push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D

// StackTest: neg
@SP
A=M-1
M=-M

// StackTest: and
@SP
M=M-1
A=M
D=M
A=A-1
M=D&M

// StackTest: push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// StackTest: or
@SP
M=M-1
A=M
D=M
A=A-1
M=D|M

// StackTest: not
@SP
A=M-1
M=!M

