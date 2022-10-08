class Jugador:
    def __init__(self):
        self.nivel = 0
        self.vidas = 0
        self.nombre = ""
        self.puntos = 0
    
    def getPuntos(self):
        return int(self.puntos)

    def addPuntos(self, p):
        self.puntos = self.puntos + p

    def getNivel(self):
        return int(self.nivel)

    def setNivel(self, n):
        self.nivel = n

    def getNombre(self):
        return self.nombre

    def setNombre(self, n):
        self.nombre = n

    def getVidas(self):
        return int(self.vidas)
    
    def setVidas(self, v):
        self.vidas = v

    def getTablero(self):
        return f"|  Jugador: {self.nombre}   |   Vidas: {self.vidas}   |   Nivel: {self.nivel}   |"