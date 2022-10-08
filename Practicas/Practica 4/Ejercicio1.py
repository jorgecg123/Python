'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y 
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''
import random

lista = []

for i in range(10):
    lista.append(random.randint(1,10))

for i in range(10):
    print(f'''
    Valor:  {lista[i]}
    Cuadro: {int(lista[i])**2}
    Cubo:   {int(lista[i])**3}
    ''')