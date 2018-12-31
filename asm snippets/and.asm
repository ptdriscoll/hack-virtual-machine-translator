// reset SP to pointer below
@SP
M=M-1

// use pointer to get value and store in D
A=M
D=M

// get next pointer down, then get value and compare with D
A=A-1
M=D&M