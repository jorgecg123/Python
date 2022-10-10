import os
from jugador import Jugador
from dibuja import Dibuja
from menu import Menu
from categoria import Categoria


class Juego:

    def __init__(self):
        """__init__()
        Constructor de la clase Juego.
        """
        self.m = Menu()
        self.j1 = Jugador()
        self.ct = Categoria()
        self.db = Dibuja()
        self.bandera = True


    def comenzar(self):
        """comenzar()
        Funcion principal que ejcuta el juego, esta defiene al menu, al jugador, realiza la selección de la categoria y dibuja a el ahorcado.
        Cicla el menu principal, donde contiene la opción para comenzar, imprimir el acumulado de puntos del jugado o simplemente salir.
        Imprime la selección de categoria y permite al jugador hacer su selección.
        Cicla la opción de ingresar una letra para adivinar la palabra siempre que las vidas sean mayor a 0.
        """
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
                            else:
                                self.j1.addPuntos(1)
                        os.system('cls')
                        self.tablero()
            elif opt == 2:
                print(f'''Tu puntaje acumulado es: {self.j1.getPuntos()} puntos''')
            elif opt == 3:
                break
            self.bandera = False
    
    def tablero(self):
        """tablero()
        Esta funcion imprime en pantalla el tablero del juego, este corresponde al ahorcado, el nombre del jugador y sus vidas.
        SI glas vidas del jugador es igual a 0 entonces imprime la palabra a adivinar.
        SI el usuario adivino la palabra a adivinar, entonces lo indica como ganadaor.
        """
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