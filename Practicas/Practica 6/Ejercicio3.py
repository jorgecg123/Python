'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó $10 , 
el segundo $20, el tercero $40 y así sucesivamente. Realizar un algoritmo para determinar 
cuanto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.
'''
abono=10
total=0

for i in range (20):
    total += abono
    print(f'''Pago del més {i + 1}:  "{total}''')
print(f'''Total: {total}''')
