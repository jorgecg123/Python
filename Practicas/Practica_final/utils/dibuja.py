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
        """__init__()
        Constructor de la clase Dibuja.
        """
        self.totalVidas = 5

    def dibujaP(self, vd):
        """dibujaP()

        Args:
            vd (string): Argumento que corresponde a las vidas del jugador, estas de le restan a la longitud de la lista que contiene el ahorcado.
        """
        print(Dibuja.ls[self.totalVidas - vd])

    def getDibujoSize(self):
        """getDibujoSize()

        Returns:
            int: Retorna la longitud de la lista que contiene al ahorcado.
        """
        return int(len(Dibuja.ls))