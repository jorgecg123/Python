'''
Clase  CuentaJoven
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase Cuenta Joven que deriva de la anterior. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
Construye los siguientes métodos para la clase:
        ● Un constructor.
        ● Los setters y getters para el nuevo atributo.
        ● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad;, por lo tanto hay que crear un método 
           es Titular Válido ( ) que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso 
           contrario.
        ● Además la retirada de dinero sólo se podrá hacer si el titular es válido.
        ● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
        ● Piensa los métodos heredados de la clase madre que hay que reescribir.
'''
from persona import Persona
from cuenta import Cuenta

class CuentaJoven(Cuenta):
        
        def __init__(self, titular:Persona, cantidad ,bonificacion):
                super().__init__(titular, cantidad)
                self.__bonificacion = bonificacion

        def setBonificacion(self, bono):
                self.__bonificacion = bono

        def getBonificacion(self):
                return self.__bonificacion

        def esTitularValido():
                return (super().getTitular().esMayorDeEdad() and super().getTitular().getEdad() < 25)

        def mostrar(self):
                return f"Cuenta Joven, Titular: {super().getTitular().mostrar()}, Cantidad: {super().getCantidad()}"

        def retirar(self, retiro):
                if retiro < super().getCantidad() and self.esTitularValido():
                        super().setCantidad(super().getCantidad() - retiro)