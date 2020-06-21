from memoria import Memoria
from utils import store_in_memory



memoria = Memoria()

# Testando se está colocando na memória
store_in_memory('teste.asm', memoria)

pos = 0
for item in memoria.dados:
    print(f'Posicao {pos}, conteudo: {item}')
    pos+=1