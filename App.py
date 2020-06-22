from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook,Entry
from tkinter import*

class App:
    def __init__(self):

        # Valores registradores
        self.r = {'$0': 0, '$1': 0, '$2': 0, '$3': 0,
            '$4': 0, '$5': 0, '$6': 0, '$7': 0,
            '$8': 0, '$9': 0, '$10': 0, '$11': 0,
            '$12': 0, '$13': 0, '$14': 0, '$15': 0,
            '$16': 0, '$17': 0, '$18': 0, '$19': 0,
            '$20': 0, '$21': 0, '$22': 0, '$23': 0,
            '$24': 0, '$25': 0, '$26': 0, '$27': 0,
            '$28': 0, '$29': 0, '$30': 0, '$31': 0}

        # Valores memoria
        self.m = {0: 0, 1: 0, 2: 0, 3: 0,
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
        self.d = {40: 0, 41: 0, 42: 0, 43: 0, 44: 0, 45: 0,
            46: 0, 47: 0, 48: 0, 49: 0}

        # Valores de sinais
        self.s = {"PCEscCond": None, "PCEsc":None,  "IouD":None,
            "LerMemoria":None, "EscMem":None,"MemParaReg":None,
            "IREsc":None, "FontePC":None, "ULAOp": None,
            "ULAFonteB":None,  "ULAFonteA":None, "EscReg":None,
            "RegDst":None}

        self.window=Tk()
        self.window.title("Scale,Tabs,Table Example")
        self.window.geometry("600x400")

        self.frame2=Frame(self.window)
        self.frame2.pack(fill="both")

        self.tablayout=Notebook(self.frame2)

        #reg
        self.tab0=Frame(self.tablayout)
        self.tab0.pack(fill="both")
        self.atualiza_reg()

        #data
        self.tab1=Frame(self.tablayout)
        self.tab1.pack(fill="both")
        self.atualiza_data()

        #memoria
        self.tab2=Frame(self.tablayout)
        self.tab2.pack(fill="both")
        self.atualiza_memoria()

        #sinais
        self.tab3=Frame(self.tablayout)
        self.tab3.pack(fill="both")
        self.atualiza_sinais()        

        # Gerencia os botoes

        self.frame = Frame(self.window, width=600, height=400)

        def keypress (event):
            print(event.char)
            if event.keysym == 'Escape':
                window.destroy()
            elif event.keysym == 'Return':
                # Lugar onde escreve comandos do processador
                    # processador .process
                    # processador .informaçoes
                
                # Passar os dados corretos p/ as funçoes:
                #altera_re()
                #altera_data()
                #altera_memoria()
                #altera_sinais()
                self.r["$0"] += 1
                self.atualiza_reg()
            # Descomente para saber qual tecla foi pressionada
                keyPressed = event.keysym
                print("Você pressionou:" + keyPressed)


        #frame.bind("<KeyRelease>", keyup)
        self.frame.bind("<KeyPress>", keypress)
        self.frame.pack()
        self.frame.focus_set()

        def callback(event):
            #Ao trocar de tabela o teclado não responde
            #Ao clicar na tela o teclado volta a funcionar
            self.frame.focus_set()

        self.frame.bind("<Button-1>", callback)
        self.frame.pack()

        self.window.mainloop()

    # Funçoes que alteram dados
    def altera_registradores(self, dic_reg):
        self.r = dic_reg
        self.atualiza_reg()

    def altera_memoria(self,dic_mem):
        self.m = dic_mem
        self.atualiza_memoria()

    def altera_data(dic_data):
        self.d = dic_data
        self.atualiza_data()

    def altera_sinais(dic_sinais):
        self.s = dic_sinais
        self.atualiza_sinais()


    #atualiza_reg()
    def atualiza_reg(self):
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
                label=Label(self.tab0,text= str_reg + "= " + str(self.r[str_reg]),bg="black",fg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                self.tab0.grid_columnconfigure(column,weight=1)
                reg += 1
                
        self.tablayout.add(self.tab0,text="Reg")
        self.tablayout.pack(fill="both")
        print("inseri")
            

    #atualiza_data()
    def atualiza_data(self):
        data_aux = 40
        
        #input box Table
        for row in range(5):
            for column in range(2):
                label=Label(self.tab1,text= str(data_aux) + " = " + str(self.d[data_aux]),bg="black",fg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                self.tab1.grid_columnconfigure(column,weight=1)
                data_aux += 1
                
        self.tablayout.add(self.tab1,text="Data")
        self.tablayout.pack(fill="both")
            

    #atualiza_memoria()
    def atualiza_memoria(self):
        data_aux = 0
        
        #input box Table
        for row in range(10):
            for column in range(4):
                label=Label(self.tab2,text= str(data_aux) + " = " + str(self.m[data_aux]),bg="black",fg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                self.tab2.grid_columnconfigure(column,weight=1)
                data_aux += 1
                
        self.tablayout.add(self.tab2,text="Memoria")
        self.tablayout.pack(fill="both")
        print("finalizei mem")
            

    #atualiza_sinais()
    def atualiza_sinais(self):
        sig = 0
        aux = list(self.s.keys())
        
        #input box Table
        for row in range(5):
            for column in range(3):
                if sig >= len(aux):
                    break
                
                label=Label(self.tab3,text= str(aux[sig]) + " = " + str(self.s[aux[sig]]),bg="black",fg="white",padx=3,pady=3)
                label.grid(row=row,column=column,sticky="nsew",padx=1,pady=1)
                self.tab3.grid_columnconfigure(column,weight=1)
                sig += 1
                
        
        self.tablayout.add(self.tab3,text="Sinais")
        self.tablayout.pack(fill="both")
