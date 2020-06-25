class PC:

    def __init__(self):
        self.pc = 0
        self.pcEsc = 0
        self.pcEsCond = 0
        self.zero = 0

    def operate(self, nova_busca):
        if self.pcEsc == 0b1:
            self.pc = nova_busca
        elif self.pcEsCond & self.zero == 0b1:
            self.pc = nova_busca
            





# pece = PC()
# pece.pc = 0
# pece.pcEsc = 0
# pece.pcEsCond = 1
# pece.zero = 0
# print(pece.pc)
# pece.operate(1)

# print(pece.pc)