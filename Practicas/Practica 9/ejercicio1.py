'''
Realizar un programa que pregunte aleatoriamente una multiplicación. 
El programa debe indicar si la respuesta ha sido correcta o no ( en caso de que la respuesta sea incorrecta 
el programa tiene que mostrar cual es la respuesta correcta). El programa preguntará 10 multiplicaciones , y 
al finalizar mostrará el número de aciertos.
'''
import random as r

acum = 0

for i in range(10):
    x = r.randint(1,10)
    y = r.randint(1,10)
    resp = int(input(f''' Ingresa el resultado de {x} X {y}'''))
    if resp == (x*y):
        acum +=1
print(acum)
