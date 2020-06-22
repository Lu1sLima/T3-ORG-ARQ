import re

class RegistradorInstrucao():

    def __init__(self):
        self.instr = None
        self.binary_instr = f'{0:032b}'


    def operate(self):
        self.decodify_bin()
        
    def decodify_bin(self):
        instruction = re.split('\W+', self.instr)

        r_type = {
        # Esses tem o OPCODE = 0
        "addu":0x21,
        "and":0x24,
        "sll":0x00, 
        "srl":0x02, 
        "xor":0x26, 
        "slt":0x2a,
        }

        i_type = {
        #OPCODE será o valor que está armazenado neles
        "addiu":0x09, 
        "lui"  :0xf, #diferente
        "sw"   :0x2b, #diferente
        "lw"   :0x23, 
        "ori"  :0xd ,
        "andi" :0xc,
        }

        j_type = {
        #OPCODE será o valor que está armazenado neles
        "beq":0x4,
        "bne":0x5, 
        }

        self.binary_instr = ''
        opcode =  instruction[0]
        if opcode in r_type:

            bin_opcode = f'{0:06b}'
            rd = f'{int(instruction[1]):05b}'
            if opcode in ('sll', 'srl'):
                # sll rd, rt, shamt
                rs = f'{0:05b}' #rs é ZERO
                rt = f'{int(instruction[2]):05b}'
                shamt = f'{int(instruction[3]):05b}'
                funct = f'{int(r_type[opcode]):06b}'
                self.binary_instr = bin_opcode+rs+rt+rd+shamt+funct

            rs = f'{int(instruction[2]):05b}'
            rt = f'{int(instruction[3]):05b}'
            shamt = f'{0:05b}'
            funct = f'{int(r_type[opcode]):06b}'
            self.binary_instr = bin_opcode+rs+rt+rd+shamt+funct
        
        elif opcode in i_type:
            bin_opcode = f'{int(i_type[opcode]):06b}'

            rt = f'{int(instruction[1]):05b}'
            if opcode in ('lui'):
                rs = f'{0:05b}'
                imm = f'{int(instruction[2]):016b}'
            elif opcode in ('lw', 'sw'):
                rs = f'{int(instruction[3]):05b}'
                imm = f'{int(instruction[2]):016b}'
            
            rs = f'{int(instruction[1]):05b}'
            rt = f'{int(instruction[2]):05b}'
            imm = f'{int(instruction[3]):016b}'
            self.binary_instr = bin_opcode+rs+rt+imm
        
        else:
            bin_opcode = f'{int(j_type[opcode]):06b}'
            rs = f'{int(instruction[1]):05b}'
            rt = f'{int(instruction[2]):05b}'
            label = f'{int(instruction[3], 16):016b}'

            self.binary_instr = bin_opcode+rs+rt+label