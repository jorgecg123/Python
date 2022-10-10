'''
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
'''


from itertools import count


cadena = str(input("Ingresa un cadena: "))
dic = {}
ls = list(cadena)

for i in range(len(ls)):
    dic[(ls[i])] = cadena.count(ls[i])

print(dic)