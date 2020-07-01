##################################################################################################################################
###################                           Luís Lima, Lucas Garcia e Guilherme Santos                       ###################
##################################################################################################################################


Instruções para uso:

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
    - 1.7 - Como o código vem do basic, então não pode colocar label (a não ser o main).
    - 1.8 - Na parte de data, os dados devem começar DEPOIS do .data, em uma linha após.
- 2 - Os registradores DEVEM ser do tipo $ NÚMERO DO REGISTRADOR ($3, $5)
- 3 - Execução:
    - 3.1 - Para executar, é necessário executar o o arquivo AppScript.py.
    - 3.2 - No AppScript.py, há uma função chamada process, é nela que acontece os ciclos.
    - 3.3 - Já existe uma opção de teste que contém todos as instruções solicitadas no trabalho, e está setado para se utilizado por padrão na função
    store_in_memory.
    - 3.4 - Ao executar o arquivo AppScript.py, irá abrir uma GUI que contém informações dos REGISTRADORES, SINAIS, DADOS, MEMORIA DE INSTRUÇÃO e outras.
    - 3.5 - Ao apertar o botão "Next" na GUI, o process irá para o próximo ciclo daquela instrução