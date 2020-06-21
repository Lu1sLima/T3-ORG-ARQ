class Memoria:
    # de 0 a 39 memoria codigo
    # de 40 a 49 memoria .data 
    dados = []

    def __init__(self):
        # Fill dados with '0'
        for i in range(50):
            self.dados = self.dados + [0]

    # reduzir 0x400000
    def calc_pos_programa(self, pos):
        pos_real = (int(str(pos), 16) - int("0x400000", 16)) / 4
        pos_real = int(pos_real)

        return pos_real
    
    # reduzir 0x10010000
    def calc_pos_data(self, pos):
        pos_real = (int(str(pos), 16) - int("0x10010000", 16)) / 4
        pos_real = int(pos_real) + 40
        
        return pos_real


    def get_dado_programa(self, pos):
        pos_real = self.calc_pos_programa(pos)

        return self.dados[pos_real]

    def get_dado_data(self, pos):
        pos_real = self.calc_pos_data(pos)

        return self.dados[pos_real]


    def set_dado_programa(self, pos, dado):
        pos_array = self.calc_pos_programa(pos)
        self.dados[pos_array] = dado


    def set_dado_data(self, pos, dado):
        pos_array = self.calc_pos_data(pos)
        self.dados[pos_array] = dado
