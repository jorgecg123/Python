'''
Programa que pida un monto(pesos) e interes, si el interes es mayor al 30%, mostrar un mensaje 
"El interes ingresado es incorrecto", sino informar el importe total, el monto mas el interes (%).
'''

monto = float(input("Ingresa el monto: "))
interes = float(input("Ingresa el interes en %: "))

if interes > 30:
    print("El interes es incorrecto")
else:
    print(f'''
    Importe total: {monto + ((monto * interes) / 100)}
    ''')