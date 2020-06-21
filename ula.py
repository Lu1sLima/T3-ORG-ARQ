class ULA():
    def __init__(self):
        self.alu_operation: bin = 0b00 #pegar uma string binaria
        self.op_1: hex = None
        self.op_2: hex = None
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
        return self.op_1 - self.op_2 #aqui tm que ter zero

    def __slt_operation(self):
        if self.op_1 < self.op_2:
            self.zero = 0b1
            return None #Ver esses retornos!
        else:
            self.zero = 0b0
            return None #Ver esses retornos!

    def operate(self):
        
        if self.alu_operation == 0b00:
            return self.__add_operation(), self.zero
        elif self.alu_operation == 0b01:
            return self.__subtract_operation(), self.zero
        elif self.alu_operation == 0b10:
            if 'addu' or 'add' in self.instr:
                return self.__add_operation(), self.zero
            elif 'sub' or 'subu' in self.instr:
                return self.__subtract_operation(), self.zero
            elif 'and' in self.instr:
                return self.__and_operation(), self.zero
            elif 'or' in self.instr:
                return self.__or_operation(), self.zero
            elif 'slt' in self.instr:
                return self.__slt_operation(), self.zero
            
        return None, self.zero #Ver aqui