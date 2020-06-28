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
