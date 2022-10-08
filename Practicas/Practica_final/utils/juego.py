import os
from jugador import Jugador
from dibuja import Dibuja
from menu import Menu
from categoria import Categoria


class Juego:

    def __init__(self):
        self.m = Menu()
        self.j1 = Jugador()
        self.ct = Categoria()
        self.db = Dibuja()
        self.bandera = True


    def comenzar(self):
        os.system('cls')
        self.j1.setNombre(input("Ingresa tu nombre de jugador: "))
        while True:
            self.j1.setVidas(self.db.getDibujoSize()-1)
            opt = self.m.opts("Juego del ahorcado", "Comenzar","Visualizar marcador", "Salir", primera_vez=self.bandera)
            if opt == 1:
                os.system('cls')
                opt = self.m.opts("Selecciona una categoria", "Animales","Super heroes", "Frutas", "Salir", primera_vez=False)
                if opt == 4:
                    break
                else:
                    os.system('cls')
                    self.j1.setNivel(opt)
                    self.ct.elijePalabra(self.j1.getNivel())
                    self.tablero()
                    while self.ct.igualaListas() != True and self.j1.getVidas() > 0:
                        opt = input("Ingresa una letra: ")
                        if self.ct.existePalabra(opt):
                            print(f"Ya ingresaste la letra {opt} ")
                        else:
                            if self.ct.actPalabra(opt) != True:
                                self.j1.setVidas(self.j1.getVidas() - 1)
                                #print(f"¡Intenta nuevamente {self.j1.getNombre()} ")
                            else:
                                self.j1.addPuntos(1)
                                #print(f"¡Buena elección {self.j1.getNombre()} ")
                        os.system('cls')
                        self.tablero()
            elif opt == 2:
                print(f'''Tu puntaje acumulado es: {self.j1.getPuntos()} puntos''')
            elif opt == 3:
                break
            self.bandera = False
    
    def tablero(self):
        self.db.dibujaP(self.j1.getVidas())
        print(self.ct.getAdivina())
        print(self.j1.getTablero())
        if self.j1.getVidas() == 0:
            print(f'''¡Perdiste {self.j1.getNombre()}! La palabra a adivinar era: {self.ct.getPalabra()}''')
        if self.ct.igualaListas():
            print(f'''¡GANASTE {self.j1.getNombre()}!''')
        print("__________________")
j = Juego()
j.comenzar()