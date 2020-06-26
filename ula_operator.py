class ULA_operator():

    def __init__(self):
        self.ULAOp = None #ou 0?
        self.func = 0

    # 111: slt - Dentro do R
    # 010: sll - Dentro do R
    # 100: srl - Dentro do R
    # 110: ori, or
    # 101: xor, xori
    # 011: andi, and
    # 000: lw, sw, lui, addu, addiu
    # 001: beq, bne
    # 010: R-Type

    # R-TYPE:
    # 100000 - add - 000
    # 100100 - and - 011
    # 101010 - slt - 111
    # 000000 - sll - 010
    # 000010 - srl - 100
    # 100110 - xor - 101

    def operate(self):
        if self.ULAOp == 0b010: #Se TIPO-R
            if self.func == 0b100001: #se add
                return 0b000
            elif self.func == 0b100100: #se and
                return 0b011
            elif self.func == 0b101010: #se slt
                return 0b111
            elif self.func == 0b000000: #se sll
                return 0b010
            elif self.func == 0b000010: #se srl
                return 0b100
            else:
                return 0b101 #xor
        
        return self.ULAOp