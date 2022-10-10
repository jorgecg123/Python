'''
Obtener el cuadrado de todos los elementos en la lista = [1,2,3,4,5,6,7,8,9,10] ( utiliza map())
'''

lista = [1,2,3,4,5,6,7,8,9,10]

lista_m_2 = map(lambda x:x**2,lista)

print(list(lista_m_2))