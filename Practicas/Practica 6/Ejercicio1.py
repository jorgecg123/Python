'''
Realizar un ejemplo de menú. donde podamos escoger las distintas opciones hasta que seleccionemos la opción "Salir".
'''
bandera = True;

while bandera:
    opt = int(input(f'''>>>>>> Ingresa <<<<<<
    (1) Opcion A
    (2) Opcion B
    (3) Opcion C
    (0) Salir
    Elección: '''))
    if opt == 0:
        bandera = False
    elif opt >= 1 and opt <= 3:
        print("---> Buena elección")
    else:
        print("No existe la opcion, vuelve a elegir.")

    