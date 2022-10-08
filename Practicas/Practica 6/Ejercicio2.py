'''
Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
'''

n = int(input('Ingresa el numero:'))

limite=0
rango=2

while limite < n:
    rango+=1
    cont = 0
    for i in range(2,rango):
        if limite%i == 0:
            cont+=1
    if cont == 0:
        print(limite)
        limite+=1


