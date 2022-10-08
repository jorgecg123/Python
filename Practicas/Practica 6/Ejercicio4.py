'''
Crear una aplicación que pida un número y calcule su factorial.
'''

n = int(input("Ingresa el numero: "))
total=1

for i in range(1,n):
    total *= (i+1)

print(total)
