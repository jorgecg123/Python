'''
Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y 
las notas que han obtenido. Cada alumno pude tener distinta cantidad de notas. Guardar la información 
en un diccionario cuya claves  serán los nombres de los alumnos y los valores serán listados con las 
notas de cada alumno. El Programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre 
e irá pidiendo sus notas hasta que introduzcamos un número negativo
'''


from multiprocessing.context import BaseContext


n = int(input("Ingresa el numero de alumnos: "))
alumnos = {}
aux=[]
count = 0
bandera = True

for i in range(n):
    nombre = input(f'''Ingresa el nombre del alumno {i+1}: ''')
    while bandera:
        resp = int(input(f'''Agrega la nota {count +1}°: '''))
        if resp < 0:
            bandera = False
        else:
            aux.append(resp)
        count+=1
    alumnos[nombre] = aux
    aux = []
    count = 0
    bandera = True

print(alumnos)