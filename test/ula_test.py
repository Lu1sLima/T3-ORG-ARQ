from ..ula import ULA
import pytest


def setup():
    ula = ULA()
    ula.op_1 = 0xA
    ula.op_2 = 0xB
    
    return ula

@pytest.mark.parametrize('operation, alu_operation, op_1, op_2, expected_result, expected_zero',[
                        ('AND',         0b000,      0xA,   0xB,     0xA,            0b0),
                        ('OR',          0b001,      0xA,   0xB,     0xB,            0b0),
                        ('ADD',         0b010,      0xA,   0xB,     0x15,           0b0),
                        ('SUBTRACT',    0b110,      0xA,   0xB,     -0x1,           0b0),
                        ('SLT',         0b111,      0xA,   0xB,     None,           0b1),

])
def test_ula(operation, alu_operation, op_1, op_2, expected_result, expected_zero):
    ula = ULA()
    ula.op_1 = op_1
    ula.op_2 = op_2
    ula.alu_operation = alu_operation

    result, zero = ula.operate()

    assert result == expected_result
    assert zero == expected_zero


# def test_ula_and():
#     #ula_operation is 0
#     ula = setup()

#     # op_1 = 1010
#     # op_2 = 1011
#     # and -> 1010 == 0xA

#     result, zero = ula.operate()

#     assert result == 0xA
#     assert zero == 0b000 # Mostrando que zero nao importa

# def test_ula_or():
#     ula = setup()
#     ula.alu_operation = 0b001

#     # op_1 = 1010
#     # op_2 = 1011
#     # and -> 1011 = 0xB

#     result, zero = ula.operate()

#     assert result == 0xB
#     assert zero == 0

