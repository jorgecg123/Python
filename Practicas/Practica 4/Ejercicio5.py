''''
Crear una tupla con los meses del año, pide números al usuarios, si el número está entre 1 
y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje 
de error. El programa termina cuando el usuario introduce un cero.
'''

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
opt = 1

while opt > 0:
    opt = int(input(f'''Ingresa un numero del 1 al {len(meses)}: '''))

    if opt >= 1 and opt <= int(len(meses)):
        print(meses[(opt-1)])
    else:
        print("Opcion no existe")