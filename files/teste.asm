.text
.globl main
main:
    lui $1, 0x00001001
    ori $10, $1, 0x00000000
    lui $1, 0x00001001
    ori $11, $1, 0x00000004
    lw $10, 0x00000000($10)
    lw $11, 0x00000000($11)
    xor $7, $10, $11
    and $8, $10, $11
    andi $12, $10, 2
    addu $9, $10, $11
    addiu $10, $9, 10
    lui $1, 0x00001001
    ori $15, $1, 0x00000000
    sw $10, 0($15)
.data
    A: .word	30
    B: .word	5
    c: .word 123
