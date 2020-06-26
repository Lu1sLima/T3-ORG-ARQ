from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
from tkinter import*

from memoria import Memoria
from ula import ULA
from controle import Controle
from utils import extend_my_bits,shift_l_my_bits,store_in_memory, Handler
from registrador_instrucao import RegistradorInstrucao
from reg_data_mem import RegDados
from saida_ula import Saida_ULA
from ula_operator import ULA_operator
from register import Register
from pc import PC

window=Tk()
window.title("Scale,Tabs,Table Example")
window.geometry("600x400")

frame2=Frame(window)
frame2.pack(fill="both")

tablayout=Notebook(frame2)

# Valores registradores
# r = {'$0': 10, '$1': 0, '$2': 0, '$3': 0,
#      '$4': 0, '$5': 0, '$6': 0, '$7': 0,
#      '$8': 0, '$9': 0, '$10': 0, '$11': 0,
#      '$12': 0, '$13': 0, '$14': 0, '$15': 0,
#      '$16': 0, '$17': 0, '$18': 0, '$19': 0,
#      '$20': 0, '$21': 0, '$22': 0, '$23': 0,
#      '$24': 0, '$25': 0, '$26': 0, '$27': 0,
#      '$28': 0, '$29': 0, '$30': 0, '$31': 0}

r = [1] * 32

# Valores memoria
# m = {0: 0, 1: 0, 2: 0, 3: 0,
#      4: 0, 5: 0, 6: 0, 7: 0,
#      8: 0, 9: 0, 10: 0, 11: 0,
#      12: 0, 13: 0, 14: 0, 15: 0,
#      16: 0, 17: 0, 18: 0, 19: 0,
#      20: 0, 21: 0, 22: 0, 23: 0,
#      24: 0, 25: 0, 26: 0, 27: 0,
#      28: 0, 29: 0, 30: 0, 31: 0,
#      32: 0, 33: 0, 34: 0, 35: 0,
#      36: 0, 37: 0, 38: 0, 39: 0}

# Valores .data
# d = {40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0,
#      46: 0, 47: 0, 48: 0, 49: 0}

# Valores de sinais
s = {"PCEscCond": None, "PCEsc":0b1,  "IouD":0b0, "LerMemoria":0b1, "EscMem":None,"MemParaReg":None, "IREsc":0b1, 
            "FontePC":0b00, "ULAOp": 0b00, "ULAFonteB":0b01,  "ULAFonteA":0b0, "EscReg":None, "RegDst":None}

# Funçoes que alteram dados
def altera_registradores(dic_reg):
    r = dic_reg
    atualiza_reg()

def altera_memoria(dic_mem):
    m = dic_mem
    atualiza_memoria()

def altera_data(dic_data):
    d = dic_data
    atualiza_data()

def altera_sinais(dic_sinais):
    s = dic_sinais
    atualiza_sinais()

ula = ULA()
controle = Controle()
sinais = controle.dic_saida
bloco_controle = s
banco_registradores = Register()
registrador_instrucao = RegistradorInstrucao()
reg_dados = RegDados()
memoria = Memoria()
pece = PC()
saida_ula = Saida_ULA()
operacao_da_ula = ULA_operator()

store_in_memory('teste2.asm', memoria)

sinais_grid = Handler()
sinais_grid.hand = s

def process():

    pc = pece.pc #PC

    ##################### Apensar para fins d debug #####################

    if 'addu' in registrador_instrucao.instr:
        controle.estado_atual
    print(f'PC {pc}')
    print(f'Estado atual {controle.estado_atual}')

    #####################################################################

    bloco_controle = controle.saida() #Pegando o dicionário com os sinais de acordo com o estado
    sinais_grid.hand = bloco_controle #Apenas para atualizar o grid no Tkinter

    mux_pc = {
        0:pc,
        1:saida_ula.saida
    }

    #Colocando os sinais na Memória
    memoria.lerMem = bloco_controle['LerMemoria']
    memoria.escMem = bloco_controle['EscMem']

    #Se não é instruçao ou dado, então nao farei nada (nao buscarei nada na memória)
    if bloco_controle['IouD'] is None:
        memoria.endereco = None
    else:
        #Buscando dado na memória a partir do resultado de saída do mux_pc
        memoria.endereco = mux_pc[bloco_controle['IouD']]
    
    
    registrador_instrucao.IREsc = bloco_controle['IREsc'] #Sinal de controle do registrador de instrução
    registrador_instrucao.operate(memoria.operate()) #Pega a instrução da memória e codifica em binário

    reg_dados.dado_lido = memoria.operate() #Registrador de dados da memória (utilizado em SW e LW) TESTAR!!
    
    #Apenas para fins de DEBUG
    print('Instrucao: '+str(registrador_instrucao.instr))

    #Enviando a instrução para o bloco de controle
    #Aqui nós enviamos a instrução literal em string('lui $2, 4') e também a instrução codificada em binário
    controle.comando = (registrador_instrucao.instr, registrador_instrucao.binary_instr)

    mux_reg_esc = { #Escolhe de que parte da instrução binária virá o registrador destino
        0:registrador_instrucao.binary_instr[11:16],
        1:registrador_instrucao.binary_instr[16:21]
    }

    mux_reg_dado = { #Escolhe de onde virá o dado para escrita em registrador
        0:saida_ula.saida,
        1:reg_dados.dado_lido
    }

    #Colocando os dados no banco de registradores
    banco_registradores.read_register1 = int(registrador_instrucao.binary_instr[6:11], 2)
    banco_registradores.read_register2 = int(registrador_instrucao.binary_instr[11:16], 2)
    banco_registradores.write_register = int(mux_reg_esc[bloco_controle['RegDst']], 2) #Registrador destino
    banco_registradores.write_data = mux_reg_dado[bloco_controle['MemParaReg']] #Dado de escrita
    banco_registradores.reg_write = bloco_controle['EscReg'] #Sinal de controle do bloco de registradores

    #Pegando a saida B do banco de registradores e passando para Dado a ser escrito na memória (É DONT CARE, PQ DEPENDE DO SINAL DE CONTROLE)
    memoria.dado_escrever = banco_registradores.read_register2

    extended_bits = extend_my_bits(registrador_instrucao.binary_instr[16:]) #Extende um binário para 32bits
    shif_my_bits = f'{shift_l_my_bits(extended_bits):032b}' #Recebe um binário(string), transforma para inteiro, faz o shift para esquerda de 2 bits e vira binario novamente

    #Pegando a saida do banco de registradores
    saida_reg_1, saida_reg_2 = banco_registradores.operate()

    mux_ula1 = {
        #MUX para saber da onde virá o primeiro operador da ula
        0:pc,
        1:int(hex(saida_reg_1), 16) #Dado vem do dado lido do registrador #1
    }

    mux_ula2 = {
        #MUX para saber da onde virá o segundo operador da ula
        0:int(hex(saida_reg_2), 16), #Vem do dado lido do registrador a ser lido #2
        1:1, #Para pc++
        2:int(extended_bits, 2), #Transforma o binário de 32 bits em inteiro
        3:int(shif_my_bits, 2) #Transforma o binário que foi shiftado 2 bits para esquerda em inteiro
    }


    #Bloco que determina a operação da ULA
    # 111: slt - Dentro do R
    # 010: sll - Dentro do R
    # 100: srl - Dentro do R
    # 101: andi, and
    # 110: xor, xori
    # 011: ori, or
    # 000: lw, sw, lui, addu, addiu
    # 001: beq, bne
    # 010: R-Type
    operacao_da_ula.ULAOp = bloco_controle['ULAOp']

    # Pegando os operadores da ula a partir da saída dos MUXs
    ula.op_1 = mux_ula1[bloco_controle['ULAFonteA']]
    ula.op_2 = mux_ula2[bloco_controle['ULAFonteB']]
    
    # Sinal de controle para operação na ULA
    ula.alu_operation = operacao_da_ula.operate()

    # Apenas para nao dar erro em algumas instruções especiais, tipo LUI, que usa o ADD mas faz um shift de 16 bits
    # Além disso, nós não precisamos da instrução para realizar as duas primeiras etapas (BUSCA E DECODIFICAÇÃO), que seriam estados 0 e 1
    if controle.estado_atual <= 1:
        ula.instr = ''
    else:
    # Agora precisamos da instrução dentro da ULA, para casos especiais (lui, ori)
        ula.instr = registrador_instrucao.instr

    # Opera a ULA com resultado e flag de zero
    saida_ula_atual, zero = ula.operate()

    # Colocando a flag de zero dentro do bloco que faz o  (PCEsc AND (zero or PCEscCond)) PARA SALTOS CONDICIONAIS E INCONDICIONAIS --- TESTAR!
    pece.zero = zero

    # Se encontrarmos instruções que mexem com o data precisamos ajeitar a posição para ficar entre 40-49 dentro do array
    if saida_ula_atual:
        if '0x1001' in hex(saida_ula_atual) and 'ori' in registrador_instrucao.instr:
            saida_ula_atual = memoria.calc_pos_data(hex(saida_ula_atual))

    mux_saida_ula = {
        0:saida_ula_atual, # Saida da operação realizada AGORA na ULA
        1:saida_ula.saida, # Saida da operação realizada ANTERIORMENTE na ULA
        # 2:None #Nao tem necessidade, pois É USADO PARA JUMP, e não tem no trabalho
    }

    # Atualizando o bloco de SAIDA_ULA(Armazenamento da função ATUAL para ser usado na PRÓXIMA FUNCAO)
    saida_ula.saida = saida_ula_atual

    # Sinais de controle de PC (PARA FAZER O AND E OR)
    pece.pcEsCond = bloco_controle['PCEscCond']
    pece.pcEsc = bloco_controle['PCEsc']

    if bloco_controle['FontePC'] is not None:
        # Atualizando o valor de PC - NÃO TESTEI DESVIOS CONDICIONAIS E INCONDICIONAIS
        pece.operate(mux_saida_ula[bloco_controle['FontePC']])




    #falta colocar o registrador de dados da memória


#reg
tab0=Frame(tablayout)
tab0.pack(fill="both")

existe_reg = False

def atualiza_reg():
    reg = 0
    
    #input box Table
    for row in range(8):
        for column in range(4):
            """
            if row==0:
                label = Entry(tab1, text="Heading : " + str(column))
                label.config(font=('Arial',14))
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                tab1.grid_columnconfigure(column, weight=1)
            else:
                #label=Entry(tab1,text="Row : "+str(row)+" , Column : "+str(column))
                #label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                #tab1.grid_columnconfigure(column,weight=1)"""
            str_reg = "$" + str(reg)
            label=Label(tab0,text= str_reg + "= " + str(banco_registradores.registers[reg]),bg="black",fg="white",padx=3,pady=3)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab0.grid_columnconfigure(column,weight=1)
            reg += 1
            
    tablayout.add(tab0,text="Reg")
    tablayout.pack(fill="both")
        
atualiza_reg()


#data
tab1=Frame(tablayout)
tab1.pack(fill="both")

def atualiza_data():
    data_aux = 40
    
    #input box Table
    for row in range(5):
        for column in range(2):
            label=Label(tab1,text= str(data_aux) + " = " + str(memoria.dados[data_aux]),bg="black",fg="white",padx=3,pady=3)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column,weight=1)
            data_aux += 1
            
    tablayout.add(tab1,text="Data")
    tablayout.pack(fill="both")
        
atualiza_data()


#memoria
tab2=Frame(tablayout)
tab2.pack(fill="both")

def atualiza_memoria():
    data_aux = 0
    
    #input box Table
    for row in range(10):
        for column in range(4):
            label=Label(tab2,text= str(data_aux) + " = " + str(memoria.dados[data_aux]),bg="black",fg="white",padx=3,pady=3)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab2.grid_columnconfigure(column,weight=1)
            data_aux += 1
            
    tablayout.add(tab2,text="Memoria")
    tablayout.pack(fill="both")
        
atualiza_memoria()


#sinais
tab3=Frame(tablayout)
tab3.pack(fill="both")

def atualiza_sinais():
    sig = 0
    aux = list(s.keys())
    
    #input box Table
    for row in range(5):
        for column in range(3):
            if sig >= len(aux):
                break
            
            dictio = sinais_grid.hand
            output = dictio[aux[sig]]
            if output == None:
                output = str(output)
            else:
                output = bin(output)
            label=Label(tab3,text= str(aux[sig]) + " = " + output,bg="black",fg="white",padx=3,pady=3)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab3.grid_columnconfigure(column,weight=1)
            sig += 1
            
    
    tablayout.add(tab3,text="Sinais")
    tablayout.pack(fill="both")
        
atualiza_sinais()


frame = Frame(window, width=600, height=400)

def keypress (event):
    print(event.char)
    if event.keysym == 'Escape':
        window.destroy()
    elif event.keysym == 'Return':
        # Lugar onde escreve comandos do processador
            # processador .process
            # processador .informaçoes
        process()
        atualiza_sinais()
        atualiza_data()
        atualiza_memoria()
        atualiza_reg()

        # Passar os dados corretos p/ as funçoes:
        
    # Descomente para saber qual tecla foi pressionada
    #keyPressed = event.keysym
    #print("Você pressionou:" + keyPressed)

# frame.bind("<KeyRelease>", keyup)
frame.bind("<KeyPress>", keypress)
frame.pack()
frame.focus_set()

def callback(event):
    #Ao trocar de tabela o teclado não responde
    #Ao clicar na tela o teclado volta a funcionar
    frame.focus_set()

frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()
