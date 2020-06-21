.data
    a: .word 12 13 14 15
    b: .asciiz "Meu amigo, mas que loucura"
    
.text
.globl main
main:
    addiu $3, $3, $3
    lw $3, 0($2)
