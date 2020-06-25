from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
from tkinter import*

from memoria import Memoria
from ula import ULA
from controle import Controle
from utils import extend_my_bits,shift_l_my_bits,store_in_memory, Handler
from registrador_instrucao import RegistradorInstrucao
from reg_data_mem import RegDados
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
store_in_memory('teste2.asm', memoria)

sinais_grid = Handler()
sinais_grid.hand = s

def process():
    pc = pece.pc

    #Pegando os sinais do estado atual

    bloco_controle = controle.saida()
    sinais_grid.hand = bloco_controle
    print(f'PC {pc}')
    print(f'Estado atual {controle.estado_atual}')

    mux_pc = {
        0:pc,
        1:ula.operate()[0]
    }

    #Colocando os sinais na Memória
    memoria.lerMem = bloco_controle['LerMemoria']
    memoria.escMem = bloco_controle['EscMem']

    #Se não é instruçao ou dado, então nao farei nada
    if bloco_controle['IouD'] is None:
        memoria.endereco = None
    else:
        #Se é instrucao ou dado, então vejo a saida do MUX_PC
        memoria.endereco = mux_pc[bloco_controle['IouD']]

    #Estado 1 é o da busca da instrução
    registrador_instrucao.IREsc = bloco_controle['IREsc']
    registrador_instrucao.operate(memoria.operate())

    reg_dados.dado_lido = memoria.operate()
    
    print('Instrucao: '+str(registrador_instrucao.instr))

    #Enviando a instrução para o bloco de controle
    controle.comando = (registrador_instrucao.instr, registrador_instrucao.binary_instr)

    mux_reg_esc = {
        0:registrador_instrucao.binary_instr[11:16],
        1:registrador_instrucao.binary_instr[16:21]
    }

    mux_reg_dado = {
        0:ula.operate()[0],
        1:reg_dados.dado_lido
    }

    banco_registradores.read_register1 = int(registrador_instrucao.binary_instr[6:11], 2)
    banco_registradores.read_register2 = int(registrador_instrucao.binary_instr[11:16], 2)
    banco_registradores.write_register = int(mux_reg_esc[bloco_controle['RegDst']], 2)
    banco_registradores.write_data = mux_reg_dado[bloco_controle['MemParaReg']]
    banco_registradores.reg_write = bloco_controle['EscReg']

    extended_bits = extend_my_bits(registrador_instrucao.binary_instr[16:]) #retorna um binario com 32 bits
    shif_my_bits = f'{shift_l_my_bits(extended_bits):032b}'

    saida_reg_1, saida_reg_2 = banco_registradores.operate()

    mux_ula1 = {
        0:pc,
        1:int(hex(saida_reg_1), 16) #digamos que terá hexadecimais no banco de registradores
    }

    mux_ula2 = {
        0:int(hex(saida_reg_2), 16),
        1:1, #para pc++
        2:int(extended_bits, 2),
        3:int(shif_my_bits, 2)
    }

    ula.op_1 = mux_ula1[bloco_controle['ULAFonteA']]
    ula.op_2 = mux_ula2[bloco_controle['ULAFonteB']]
    ula.alu_operation = bloco_controle['ULAOp']
    ula.instr = registrador_instrucao.instr

    saida_ula, zero = ula.operate()

    mux_saida_ula = {
        0:ula.operate()[0],
        1:ula.operate()[0],#ver isso
        2:None
    }
    
    if bloco_controle['FontePC'] is not None:
        pece.operate(mux_saida_ula[bloco_controle['FontePC']])
    print(pc)




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

# btn1 = Button(window, text='Press', fg='white',   bg='black', font=('comicsans', 12), command=process(pc)).pack()
# btn1.pack(side = BOTTOM)
# Gerencia os botoes

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
