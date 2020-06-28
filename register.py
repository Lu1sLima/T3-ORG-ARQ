


class Register():

    def __init__(self, read_register1=0, read_register2=0, write_register=0, write_data=0):
        '''
            Register must be integer!
        '''
        self.registers = [0] * 32
        self.reg_write: bin = 0b0 #mudar pra satring
        self.read_register1 = read_register1
        self.read_register2 = read_register2
        self.write_register = write_register
        self.write_data     = write_data

    def __read_data(self) -> tuple:
        '''
            Search data of specific register in registers array.

            Return: a tuple with read data
        '''

        reg_data1 = self.registers[self.read_register1]
        reg_data2 = self.registers[self.read_register2]

    #VER SE ISSO VAI BUGAR
        return int(reg_data1), int(reg_data2)

    def __write_data(self):
        '''Aqui eu apenas verifico se o regWrite é mesmo 1, e se sim, vou no banco de registradores (ARRAY) 
        com a posição do registrador destino e escrevo o dado'''

        if self.reg_write == 0b1:
            self.registers[self.write_register] = self.write_data
        
        return 0, 0


    def operate(self):

        if self.reg_write == 0b0:
            return self.__read_data()
        elif self.reg_write == 0b1:
            return self.__write_data()
        return 0, 0



