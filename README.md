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
- :white_check_mark: **beq: com saltos negativos e positivos**
- :white_check_mark: **bne: com saltos negativos e positivos**
- :white_check_mark: **srl**
- :white_check_mark: **sll**
- :white_check_mark:  **slt**


## INSTRUÇÕES PARA USO

- 1 - Arquivo de entrada:
    - 1.1 - O Arquivo de entrada DEVE seguir o padrão do arquivo teste.asm.
    - 1.2 - O Arquivo de entrada DEVE ter as 3 primeiras linhas no seguinte sentido:
            .text
            .globl main
            main:
            AQUI SE INICIA AS INSTRUÇÕES
    - 1.3 - As instruções DEVEM começar APÓS o main, ou seja, é necessário que comecem na próxima linha depois da label main.
    - 1.4 - As instruções DEVEM ser do basic.
    - 1.5 - Os arquivos de entrada devem ser preferívelmente do tipo .asm.
    - 1.6 - O arquivo de teste DEVE ESTAR na pasta files e tem que se chamar teste.asm, caso queira chamar outro arquivo deverá mudar na função store_in_memory
    dentro do arquivo AppScript.py.
    - 1.7 - Como o código vem do basic, então é não pode colocar label (a não ser o main).
- 2 - Os registradores DEVEM ser do tipo $ NÚMERO DO REGISTRADOR ($3, $5)
- 3 - Execução:
    - 3.1 - Para executar, é necessário rodar o comando (o arquivo AppScript.py).
    - 3.2 - No AppScript.py, há uma função chamada process, é nela que acontece os ciclos.
    - 3.3 - Já existe uma opção de teste que contém todos as instruções solicitadas no trabalho, e está setado para se utilizado por padrão na função
    store_in_memory.
    - 3.4 - Ao executar o arquivo AppScript.py, irá abrir uma GUI que contém informações dos REGISTRADORES, SINAIS, DADOS, MEMORIA DE INSTRUÇÃO e outras.
    - 3.5 - Ao apertar o botão "Next" na GUI, o process irá para o próximo ciclo daquela instrução

## EXPLICAÇÃO DO ARQUIVO DE TESTE
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
    beq $0, $10, 0xffffffed # No momento nao acontece nada, pois a comparação vai ser FALSA e nao vai saltar, se tu colocar uma comparação verdadeira beq $0, $0, 0xffffffed por exemplo, ele vai saltar para o MAIN (pc = 0), primeira intrução.
    slt $18, $0, $10 #testa se o dado que está em $0(Que é zero) é menor do que está em $10 (que é 45), se sim, coloca 1 em $18
.data
    A: .word	30
    B: .word	5
    c: .word 123

```
