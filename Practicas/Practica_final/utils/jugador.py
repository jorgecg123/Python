class Jugador:
    def __init__(self):
        """__init__()
        Constructor de la clase Jugador.
        """
        self.nivel = 0
        self.vidas = 0
        self.nombre = ""
        self.puntos = 0
    
    def getPuntos(self) -> int:
        """getPuntos()

        Returns:
            int: Retorna la cantidad de puntos acumulados por el jugador.
        """
        return int(self.puntos)

    def addPuntos(self, p):
        """addPuntos()

        Args:
            p (int): Recibe los puntos que se le sumaran al puntaje del jugador.
        """
        self.puntos = self.puntos + p

    def getNivel(self) -> int:
        """getNivel()

        Returns:
            int: Retorna el nivel seleccionado por el jugador.
        """
        return int(self.nivel)

    def setNivel(self, n):
        """setNivel()

        Args:
            n (int): Recibe el nivel selecionado por el jugador.
        """
        self.nivel = n

    def getNombre(self) -> str:
        """getNombre()

        Returns:
            str: Retorna el nombre de usuario ingresado por el jugador.
        """
        return self.nombre

    def setNombre(self, n):
        """setNombre()

        Args:
            n (str): Recibe el nombre de usuario ingresado por el jugador.
        """
        self.nombre = n

    def getVidas(self) -> int:
        """getVidas()

        Returns:
            int: Retorna el numero de vidas del jugador.
        """
        return int(self.vidas)
    
    def setVidas(self, v):
        """setVidas()

        Args:
            v (int): Recibe el numero de vidas del jugador.
        """
        self.vidas = v

    def getTablero(self) -> str:
        """getTablero()

        Returns:
            str: Retorna el tabledo con el nombre, vidas y nivel del jugador.
        """
        return f"|  Jugador: {self.nombre}   |   Vidas: {self.vidas}   |   Nivel: {self.nivel}   |"