class ULA():
    def __init__(self):
        self.alu_operation: bin = 0b00 #pegar uma string binaria
        self.op_1: hex = 0b0
        self.op_2: hex = 0b0
        self.zero: bin = 0b0
        self.instr: str = ''
        #Talvez ter uma tributo de ula_saida?


    def __and_operation(self):
        '''
            Used for: and
        '''
        return self.op_1 & self.op_2

    def __or_operation(self):
        '''
            Used for: or
        '''
        return self.op_1 | self.op_2

    def __add_operation(self):
        '''
            Used for: add, lw and sw
        '''
        return self.op_1 + self.op_2

    def __subtract_operation(self):
        '''
            Used for: sub, beq
        '''
        sub = self.op_1 - self.op_2
        if sub == 0:
            self.zero = 1
        return sub #aqui tm que ter zero

    def __slt_operation(self):
        if self.op_1 < self.op_2:
            self.zero = 0b1
            return None #Ver esses retornos!
        else:
            self.zero = 0b0
            return None #Ver esses retornos!

    def __xor_operation(self):
        return self.op_1 ^ self.op_2

    def __srl_operation(self):
        return self.op_1 >> self.op_2 #VER ISSO

    def __sll_operation(self):
        return self.op_1 << self.op_2 #VER ISSO

    def operate(self):
        if self.alu_operation == 0b000:
            return self.__add_operation(), self.zero
        elif self.alu_operation == 0b001:
            return self.__subtract_operation(), self.zero
        elif self.alu_operation == 0b011:
            return self.__and_operation(), self.zero
        elif self.alu_operation == 0b101:
            return self.__xor_operation(), self.zero
        elif self.alu_operation == 0b110:
            return self.__or_operation(), self.zero
        elif self.alu_operation == 0b111:
            return self.__slt_operation(), self.zero
        elif self.alu_operation == 0b010:
            return self.__sll_operation(), self.zero
        elif self.alu_operation == 0b100:
            return self.__srl_operation(), self.zero
            
        return None, self.zero #Ver aqui