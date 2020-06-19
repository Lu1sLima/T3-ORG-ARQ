from ..register import Register
from ..ula import ULA
import pytest



@pytest.mark.parametrize('operation, alu_operation, reg12_content,   reg4_content, expected_zero',[
                        ('AND',         0b000,      0xA,                0xB,              0b0),
                        ('OR',          0b001,      0xA,                0xB,              0b0),
                        ('ADD',         0b010,      0xA,                0xB,              0b0),
                        ('SUBTRACT',    0b110,      0xA,                0xB,              0b0),

])
def test_register_ula(operation, alu_operation, reg12_content, reg4_content, expected_zero):
    registers = Register(read_register1=12, read_register2=4, write_register=1)
    registers.registers[12] = reg12_content #Em $12 terá esse valor
    registers.registers[4] = reg12_content #Em $4 terá esse valor
    registers.write_register = 1 #$1 é o registrador destino

    op_1, op_2 = registers.operate() #Pegando os valores dos registradores $12 e $4
    ula = ULA()
    ula.alu_operation = alu_operation #Qual operação será
    ula.op_1 = op_1 #$12 na entrada 1 da ula
    ula.op_2 = op_2 #$4 na entrada 2 da ula

    saida_ula, zero = ula.operate() #Fazendo a operação na ula

    registers.write_data = saida_ula # Colocando a saida da ula no dado para ser escrito
    registers.reg_write = 0b1 # Controlador de escrita no registrador em 1

    registers.operate() #Salvando no registrador destino $1

    assert registers.registers[1] == saida_ula