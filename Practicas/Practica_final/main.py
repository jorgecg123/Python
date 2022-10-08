import os
from models.jugador import Jugador

from utils.dibuja import Dibuja
from utils.menu import Menu
from models.categoria import Categoria


def main():
    m = Menu()
    j1 = Jugador()
    ct = Categoria()
    db = Dibuja()

    bandera = True
    while True:
        os.system('cls')
        opt = m.opts("Juego del ahorcado", "Comenzar",
                  "Visualizar marcador", "Salir", primera_vez=bandera)
        if opt == 3:
            break
        if opt == 1:
            os.system('cls')
            nivel = m.opts("Selecciona la categoria", "Animales",
                  "Super heroes", "Frutas" ,"Salir", primera_vez=False)
            j1.setNombre(input("Ingresa tu nombre de jugador: "))
            if nivel == 4:
                break
            else:
                os.system('cls')
                j1.setNivel(nivel)
                ct.elijePalabra(nivel)
                while ct.igualaListas() != True and j1.getVidas() > 0:
                    os.system('cls')
                    db.dibujaP(j1.getVidas())
                    print(ct.getAdivina())
                    print(j1.getTablero())
                    opt = input("Ingresa una letra: ")
                    if ct.existePalabra(opt):
                        print(f"Ya ingresaste la letra {opt} ")
                    else:
                        if ct.actPalabra(opt) != True:
                            j1.setVidas(j1.getVidas() - 1)
                            print(f"¡Intenta nuevamente {j1.getNombre()} ")
                        else:
                            print(f"¡Buena elección {j1.getNombre()} ")
            os.system('cls')
            db.dibujaP(j1.getVidas())
            print(f"¡Perdiste {j1.getNombre()} ")
            break
        else:
            bandera = False

if __name__ == "__main__":
    main()



'''
n = Nivel(1)

n.elijePalabra()
print(n.getAdivina())

while n.igualaListas() != True:
    opt = input("Ingresa la letra: ")
    n.actPalabra(opt)
    print(n.getAdivina())
'''