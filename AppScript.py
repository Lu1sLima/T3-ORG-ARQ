from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
from tkinter import*


window=Tk()
window.title("Scale,Tabs,Table Example")
window.geometry("600x400")

frame2=Frame(window)
frame2.pack(fill="both")

tablayout=Notebook(frame2)

# Valores registradores
r = {'$0': 10, '$1': 0, '$2': 0, '$3': 0,
     '$4': 0, '$5': 0, '$6': 0, '$7': 0,
     '$8': 0, '$9': 0, '$10': 0, '$11': 0,
     '$12': 0, '$13': 0, '$14': 0, '$15': 0,
     '$16': 0, '$17': 0, '$18': 0, '$19': 0,
     '$20': 0, '$21': 0, '$22': 0, '$23': 0,
     '$24': 0, '$25': 0, '$26': 0, '$27': 0,
     '$28': 0, '$29': 0, '$30': 0, '$31': 0}

# Valores memoria
m = {0: 0, 1: 0, 2: 0, 3: 0,
     4: 0, 5: 0, 6: 0, 7: 0,
     8: 0, 9: 0, 10: 0, 11: 0,
     12: 0, 13: 0, 14: 0, 15: 0,
     16: 0, 17: 0, 18: 0, 19: 0,
     20: 0, 21: 0, 22: 0, 23: 0,
     24: 0, 25: 0, 26: 0, 27: 0,
     28: 0, 29: 0, 30: 0, 31: 0,
     32: 0, 33: 0, 34: 0, 35: 0,
     36: 0, 37: 0, 38: 0, 39: 0}

# Valores .data
d = {40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0,
     46: 0, 47: 0, 48: 0, 49: 0}

# Valores de sinais
s = {"PCEscCond": None, "PCEsc":None,  "IouD":None,
     "LerMemoria":None, "EscMem":None,"MemParaReg":None,
     "IREsc":None, "FontePC":None, "ULAOp": None,
     "ULAFonteB":None,  "ULAFonteA":None, "EscReg":None,
     "RegDst":None}

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
            label=Label(tab0,text= str_reg + "= " + str(r[str_reg]),bg="black",fg="white",padx=3,pady=3)
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
            label=Label(tab1,text= str(data_aux) + " = " + str(d[data_aux]),bg="black",fg="white",padx=3,pady=3)
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
            label=Label(tab2,text= str(data_aux) + " = " + str(m[data_aux]),bg="black",fg="white",padx=3,pady=3)
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
            
            label=Label(tab3,text= str(aux[sig]) + " = " + str(s[aux[sig]]),bg="black",fg="white",padx=3,pady=3)
            label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
            tab3.grid_columnconfigure(column,weight=1)
            sig += 1
            
    
    tablayout.add(tab3,text="Sinais")
    tablayout.pack(fill="both")
        
atualiza_sinais()


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
        
        # Passar os dados corretos p/ as funçoes:
        altera_re()
        altera_data()
        altera_memoria()
        altera_sinais()
        
    # Descomente para saber qual tecla foi pressionada
    #keyPressed = event.keysym
    #print("Você pressionou:" + keyPressed)


#frame.bind("<KeyRelease>", keyup)
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
