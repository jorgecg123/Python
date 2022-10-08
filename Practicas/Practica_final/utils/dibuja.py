class Dibuja:

    ls = [
        '''  
             +---------+
                       |
                       |
                       |
                       |
                       |
            ___________|''',
        '''  
             +---------+
             |         |
             0         |
                       |
                       |
                       |
            ___________|''',
        '''  
             +---------+
             |         |
             0         |
             |         |
                       |
                       |
            ___________|''',
        '''  
             +---------+
             |         |
             0         |
            /|\        |
                       |
                       |
            ___________|''',
        '''  
             +---------+
             |         |
             0         |
            /|\        |
             '         |
                       |
            ___________|''',
        '''  
             +---------+
             |         |
             0         |
            /|\        |
            /'\        |
                       |
            ___________|'''
    ]


    def __init__(self):
        self.totalVidas = 5

    def dibujaP(self, vd):
        print(Dibuja.ls[self.totalVidas - vd])
    def getDibujoSize(self):
        return int(len(Dibuja.ls))