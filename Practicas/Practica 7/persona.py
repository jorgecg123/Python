'''
Clase Persona
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Contruye los siguentes métodos para la clase:
        1.- Un constructor, donde los datos pueden estar vacíos.
        2.- Los setters y getters para cada uno de los atributos. Hay que validar las entrada de datos.
        3.- mostrar(): Muestre los datos de la persona. 
        4.- esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:

    def __init__(self):
        self.nombre=""
        self.edad=0
        self.DNI=""

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setDNI(self, dni):
        self.DNI = dni

    def getDNI(self):
        return self.DNI
    
    def mostrar(self):
        return f"Nombre: {self.getNombre()}, Edad: {self.getEdad()}, DNI: {self.getDNI()}"

    def esMayorDeEdad(self):
        return (self.getEdad() > 18)