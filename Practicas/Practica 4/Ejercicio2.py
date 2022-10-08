'''
Crear una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por pantalla.
'''

lista = []
lista2 = []

for i in range(5):
    lista.append(input(f'''Ingresa la {i+1}° cadena: '''))

for i in range(5):
    lista2.append(lista[-(i+1)])

print(lista2)