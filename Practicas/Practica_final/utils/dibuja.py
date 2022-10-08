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
        #self.nivel = 0
        #self.vidas = 5
    
    #def setVidas(self, v):
        #self.vidas = v

    #def getVidas(self):
        #return int(self.vidas)

    #def getNivel(self):
        #return int(self.nivel)

    #def setNivel(self, n):
        #self.nivel = n

    def dibujaP(self, vd):
        print(Dibuja.ls[self.totalVidas - vd])
        #print(f" >>>>  Nivel: {self.nivel}  <<<->>>  Vidas restantes: {self.getVidas()}  <<<< ")