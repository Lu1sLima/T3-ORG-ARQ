class Controle():
    
    def __init__(self):
        self.estado_atual = 0
        self.dic_saida = {
            0: self.saida0,
            1: self.saida1,
            2: self.saida2,
            3: self.saida3,
            4: self.saida4,
            5: self.saida5,
            6: self.saida6,
            7: self.saida7,
            8: self.saida8,
            9: self.saida9
        }
        self.comando = ""
        
    def insere_comando(self, comando):
        self.comando = comando


    def saida(self):
        # print(self.estado_atual)
        return self.dic_saida[self.estado_atual]()

    def saida0(self):
        saida = {
            "PCEscCond": None, "PCEsc":0b1,  "IouD":0b0, "LerMemoria":0b1, "EscMem":None,"MemParaReg":None, "IREsc":0b1, 
            "FontePC":0b00, "ULAOp": 0b00, "ULAFonteB":0b01,  "ULAFonteA":0b0, "EscReg":None, "RegDst":None
        }
        self.estado_atual = 1
        return saida

    def saida1(self):
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":None, "IREsc":None,
            "FontePC":None, "ULAOp": 0b00, "ULAFonteB":0b11, "ULAFonteA":0b0, "EscReg":None, "RegDst":None
            }

        if "lw" in self.comando[0] or "sw" in self.comando[0]:
            self.estado_atual = 2
        elif "beq" in self.comando[0]:
            self.estado_atual = 8
        elif int(self.comando[1][0:6], 2) == 0:
            # Caso seja tipo r
            self.estado_atual = 6
        else:
            #caso seja tipo i
            True == True

        return saida

    def saida2(self):
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":None, "IREsc":None,
            "FontePC":None, "ULAOp": 0b00, "ULAFonteB":0b10, "ULAFonteA":0b1, "EscReg":None, "RegDst":None
        }

        if "lw" in self.comando[0]:
            self.estado_atual = 3
        elif "sw" in self.comando[0]:
            self.estado_atual = 5

        return saida

    def saida3(self):
        # Acesso a memoria
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":0b0, "LerMemoria":0b1, "EscMem":None, "MemParaReg":None, "IREsc":None,
            "FontePC":None, "ULAOp":None, "ULAFonteB":None, "ULAFonteA":None, "EscReg":None, "RegDst":None
        }
        self.estado_atual = 4
        return saida

    def saida4(self):
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":0b1, "IREsc":None, 
            "FontePC":None, "ULAOp":None, "ULAFonteB":None, "ULAFonteA":None, "EscReg":0b1,"RegDst":0
        }
        self.estado_atual = 0
        return saida

    def saida5(self):
        #acesso a memoria
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":0b1, "LerMemoria":None, "EscMem":0b1, "MemParaReg":None, "IREsc":None,
            "FontePC":None, "ULAOp":None, "ULAFonteB":None, "ULAFonteA":None, "EscReg":None, "RegDst":None
        }
        self.estado_atual = 0
        return saida

    def saida6(self):
        #execução
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":None, "IREsc":None,
            "FontePC":None, "ULAOp":0b10, "ULAFonteB":0b00, "ULAFonteA":0b1, "EscReg":None, "RegDst":None
        }
        self.estado_atual = 7
        return saida

    def saida7(self):
        #Termino da instrução tipo R (escrita em Rd)
        saida = {
            "PCEscCond":None, "PCEsc":None, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":0b0, "IREsc": None,
            "FontePC":None, "ULAOp":None, "ULAFonteB":None, "ULAFonteA":None, "EscReg":0b1, "RegDst":0b1
        }
        self.estado_atual = 0
        return saida

    def saida8(self):
        #Termino do desvio condicional
        saida = {
            "PCEscCond":0b1, "PCEsc":0, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":None, "IREsc":None,
            "FontePC":0b01, "ULAOp": 0b01, "ULAFonteB":0b00, "ULAFonteA":1, "EscReg":None, "RegDst":None
        }
        self.estado_atual = 0
        return saida

    def saida9(self):
        self.estado_atual = 0
        saida = {
            "PCEscCond":None, "PCEsc":0b1, "IouD":None, "LerMemoria":None, "EscMem":None, "MemParaReg":None, "IREsc":None,
            "FontePC":0b01, "ULAOp":None, "ULAFonteB":None, "ULAFonteA":None, "EscReg":None, "RegDst":None
        }
        self.estado_atual = 0
        return saida


### Testa
# a = Controle()

# def p1():
#     return 2

# dict = {
#     1: p1
# }

# print(a.saida())
# print(a.saida())
###

# dic_resp = {0:1, 1:1}

# dic_entrada = {0:None, 1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None}


# for i in dic_entrada.keys():

# 	if i in dic_resp.keys():
# 		dic_entrada[i] = dic_resp[i]
# 	else:
# 		dic_entrada[i] = None

# print(dic_entrada)