# T3-ORG-ARQ




## INSTRUÇÕES FUNCIONANDO:

- :white_check_mark: **lw**
- :white_check_mark: **sw**
- :white_check_mark: **addu**
- :white_check_mark: **and**
- :white_check_mark: **andi**
- :white_check_mark: **addiu**
- :white_check_mark: **lui**
- :white_check_mark: **ori**
- :white_check_mark: **xor**
- :x: **beq**
- :x: **bne**
- :white_check_mark: **srl**
- :white_check_mark: **sll**
- :x:  **slt**


```assembly
.text
.globl main
main:
    lui $1, 0x00001001 # Inicio de la $10, A
    ori $10, $1, 0x00000000 # Término da instrução la $10, A -> Deve ter no registrador 10 o endereço de B(40)
    lui $1, 0x00001001 # Inicio de la $11, B
    ori $11, $1, 0x00000004 # Término da instrução la $11, B -> Deve ter no registrador 11 o endereço de B(41)
    lw $10, 0x00000000($10) # Lê o endereço de memória(para dados) que está no registrador $10 (que é o endereço 40), e coloca a palavra em $10. $10 deve ter 30
    lw $11, 0x00000000($11) # Lê o endereço de memória(para dados) que está no registrador $11 (que é o endereço 41), e coloca a palavra em $11. $11 deve ter 5
    xor $7, $10, $11 #30 xor 5, $7 deve ter 27
    and $8, $10, $11 # 30 and 5, $8 4
    andi $12, $10, 2 # 30 and 2, $12 deve ter 4
    addu $9, $10, $11 # 30 + 5, $9 deve ter 35
    addiu $10, $9, 10 # 35+10, $10 deve ter 45
    lui $1, 0x00001001 # Inicio de la $15, A
    ori $15, $1, 0x00000000 #Término de la $15, A, $15 deve ter o endereço de A, que é 40
    sw $10, 0($15) # Guarda o valor que está em $10(que é 45) na posicao de memória armazenada em $15(que é 40) e
    # Substitui na memória de dados a posicao 40 pelo valor que está contido em $10, que é 45, ou seja, no .data, A será 45
    lui $16, 0x0000000B # Colocando B(11) no registrador $16
    sll $16, $16, 0x00000002 # Shiftando 2 para à esquerda no dado que está no $16 (11 << 2), resultado deve ser 44 e será guardado em $16
    lui $17, 0x0000000C # Colocando C(12) no registrador $17
    srl $17, $17, 0x00000002 # Shiftando 2 para à direita no dado que está no $17 (12 >> 2), resultado deve ser 3 e será guardado em $17
.data
    A: .word	30
    B: .word	5
    c: .word 123

```
