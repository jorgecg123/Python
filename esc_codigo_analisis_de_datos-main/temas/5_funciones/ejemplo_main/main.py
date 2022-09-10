''' importar todas las funciones de funciones'''
#from funciones import *
''' importar todo el archivo y darle un alias'''
import funciones as f

def main():
    print("Hola mundo")
    print("Suma:",f.suma_n_numeros(1,2,3,4,5,6,7,8,9))
    print("Promedio:",f.promedio_n_numeros(1,2,3,4,5,6,7,8,9))
    max,min= f.maximo_minimo(4,5,8,7,2,6,9,4,3);
    print("Max:",max,"Min:",min)
    
if __name__ == "__main__":
    main()