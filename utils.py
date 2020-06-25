import re

def store_in_memory(file_name: str, memoria):
    with open(f'files\{file_name}', 'r') as file:
        lines = file.readlines()

        line = 0
        instr = 0

        #Se o arquivo começar com .text
        if '.text' in lines[0]:
            line = 3
            #Colocando as INSTRUÇÕES(.text) na memória
            while(line < len(lines)):
                if '.data' in lines[line]:
                    break

                if '$' in lines[line]:
                    instruction = lines[line].strip()
                    memoria.dados[instr] = instruction
                    instr+=1
                line += 1

            #Colocando os DADOS(.data) na memória
            data = 40
            for i in range(line+1, len(lines)):
                instruction = lines[i]

                if '.word' in instruction:
                    instruction = (instruction.split('.word')[1]).split()
                    #Se for array:
                    if len(instruction) > 1:
                        for item in instruction:
                            memoria.dados[data] = item
                            data+= 1
                    #Se nao, é um dado apenas
                    else:
                        memoria.dados[data] = instruction[0]
                        data+=1
                #Se for uma string
                elif '.asciiz' in instruction:
                    instruction = instruction.split('.asciiz ')
                    memoria.dados[data] = instruction[1]
                    data+=1

        #Se o arquivo começar com .data
        else:
            line = 1
            data = 40
            #Colocando os DADOS (.data) na memória
            while(line < len(lines)):
                if '.text' in lines[line]:
                    break

                instruction = lines[line]
                if '.word' in instruction:
                    instruction = (instruction.split('.word')[1]).split()
                    #Se for array
                    if len(instruction) > 1:
                        for item in instruction:
                            memoria.dados[data] = item
                            data+= 1
                    #Se não, é um dado apenas
                    else:
                        memoria.dados[data] = instruction[0]
                        data+=1
                #Se for string
                elif '.asciiz' in instruction:
                    instruction = instruction.split('.asciiz ')
                    memoria.dados[data] = instruction[1]
                    data+=1
                line+=1

            instr = 0
            #Colocando as INSTRUÇÕES(.text) na memória
            for i in range(line+3, len(lines)):
                if '$' in lines[i]:
                    instruction = lines[i].strip()
                    memoria.dados[instr] = instruction
                    instr+=1

    print("Arquivo carregado para memória!")
    return


def extend_my_bits(bits: str):
    return bits.zfill(32)

def shift_l_my_bits(bits:str):
    return int(bits, 2) << 2


class Handler():
    hand = 0