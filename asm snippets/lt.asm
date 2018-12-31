// reset SP to pointer below
@SP
M=M-1

// use pointer to get value and store in D
A=M
D=M

// get next pointer down, then get value and subtract D from it
A=A-1
D=M-D

// set value on stack to true as default
M=-1

// check if M-D < 0, and if so jump over setting to false
@JUMP
D;JLT

// if remainder isn't < 0, set to false
@SP
A=M-1
M=0

(JUMP)