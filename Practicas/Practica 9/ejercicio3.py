'''
Obtener la cantidad de elementos mayores a 5 en la tupla, tupal = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
'''


tupal = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

acum = 0
for i in range(len(tupal)):
    if tupal[i] > 5:
        acum +=1

print(acum)