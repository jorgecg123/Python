'''
Escribe un programa en python que pida un número por teclado y que cree un diccionario cuyas claves sean 
desde el 1 hasta el número indicado, los valores son los cuadrados de las claves
'''

n = int(input("Ingresa un numero: "))
dic = {}


for i in range(1,n):
    dic[i] = i**2

print(dic)