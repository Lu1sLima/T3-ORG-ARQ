import pytest

from unittest.mock import patch
from ..register import Register


def setup():
    register_1 = 12
    register_2 = 4
    write_register = 1
    write_data = 0x014

    register = Register(register_1, register_2, write_register, write_data)
    register.registers[register_1] = 0x0123
    register.registers[register_2] = 0x2345

    return register

def test_register_read():
    register_file = setup()

    read_data1, read_data2 = register_file.operate()

    write_register = register_file.registers[3]

    assert read_data1 == 0x0123
    assert read_data2 == 0x2345
    assert write_register == None #Verificando que não escreveu no registrador, pq o regWrite é 0

def test_register_write():
    register_file = setup()

    register_file.reg_write = 0b1

    read_data1, read_data2 = register_file.operate()

    write_register = register_file.registers[register_file.write_register]

    assert read_data1 == None
    assert read_data2 == None
    assert write_register == register_file.write_data #verificando se o registrador foi escrito
