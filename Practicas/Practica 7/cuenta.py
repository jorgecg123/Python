'''
Clase Cuenta
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
        ● Un constructor, donde los datos pueden estar vacíos.
        ● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o 
           retirando dinero.
        ● mostrar(): Muestra los datos de la cuenta.
        ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
        ● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''
from persona import Persona

class Cuenta:

    def __init__(self, titular: Persona, cantidad=0.00):
        self.__titular = titular
        self.__cantidad = cantidad

    def setTitular(self, titular:Persona):
        self.__titular = titular

    def getTitular(self) -> Persona:
        return self.__titular

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def getCantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        return f"Titular: {self.getTitular().mostrar()} Cantidad: {self.getCantidad()}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.setCantidad(self.getCantidad() + cantidad)

    def retirar(self, retiro):
        if retiro < self.getCantidad():
            self.setCantidad(self.getCantidad() - retiro)