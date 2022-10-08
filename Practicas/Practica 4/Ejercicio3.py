'''
Se quiere realizar un programa que lea por teclado las 5 notas optenidas por un alumno 
(compredidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, 
la nota más alta y la menor.
'''


notas = []
cont=0


while cont < 5:
    nota = float(input(f'''Ingresa la {cont+1}° nota: '''))
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        cont+=1


print(f'''
Media: {sum(notas)/len(notas)}
Mas alta: {max(notas)}
Menor: {min(notas)}
''')