SET R0, 0x05
SET R1, 0x00

loop:
ADD R1, R0
DEC R0
JZ halt
JMP loop

halt:
JMP halt
