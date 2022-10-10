'''
Crear un programa donde vamos a declarar un diccionario que contenga los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de 
la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
Tras cada consulta el programa nos preguntara si queremos hacer otra consulta.
'''

fruta = {
    "Manzana": 20.50,
    "Naranja": 40.55,
    "Melon": 27.50,
    "Sandia": 50.75,
    "Pera": 30.99
}

dic={}


while True:
    opt=int(input(f'''Menu
    1. Ingresar fruta
    2. Consultar
    Otro: Salir'''))
    if opt == 1:
        for llave,valor in fruta.items():
            ca = int(input(f"Ingresa la cantidad de {llave}: "))
            dic[llave] = ca * valor
    elif opt ==2:
        if dic:
            fr = input("Ingresa la fruta: ")
            if fr in dic:
                print(dic[fr])
            else:
                print("Error: la fruta no existe")
    else:
        break