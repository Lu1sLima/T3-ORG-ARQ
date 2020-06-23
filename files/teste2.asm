.text
.globl main
main:
    addu $2, $3, $7
    lw $3, 0($2)
    addu $1 $10, $5
.data
    a: .word 12 13 14 15
    b: .asciiz "Meu amigo, mas que loucura"
    c: .word 123
