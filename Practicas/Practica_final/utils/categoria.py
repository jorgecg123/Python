import random as r
from xmlrpc.client import Boolean, boolean

class Categoria:

    dic = {
        "Nivel1" : ["Avestruz", "Ballena", "Caballo", "Elefante", "Flamenco", "Guepardo", "Hiena", "Jaguar", "Koala", "Llama", "Mapache", "Nutria", "Paloma", "Rinoceronte", "Salamandra", "Tigre", "Vaca", "Zorrillo"],
        "Nivel2" : ["Spiderman", "Logan", "Superman", "Batman", "Thor", "Deadpool"],
        "Nivel3" : ["Aguacate", "Piña", "Manzana", "Naranjas", "Guayaba", "Cereza"]
    }

    def __init__(self):
        """__init__()
        Constructor de la clase Categoria.
        """
        self.palabra = ""
        self.lsPalabra = []
        self.lsAdivina = []
    

    def elijePalabra(self, nivel):
        """elijePalabra()

        Args:
            nivel (int): Es el nivel elejido por el usuario, este se iguala a la categoria del menu principal.
        """
        n="Nivel"+str(nivel)
        self.palabra = Categoria.dic[n][r.randint(0,(len(Categoria.dic[n])-1))]
        self.lsPalabra = list(self.palabra)
        self.lsAdivina = ["_" for i in self.lsPalabra] 

    def actPalabra(self, pl) -> bool:
        """actPalabra()

        Args:
            pl (string): Se refiere a la letra a buscar en la lista lsPalabra.

        Returns:
            bool: Retorna True si pl existe en lsPalabra y False en caso de no existir.
        """
        if str(pl).lower() in self.lsPalabra or str(pl).upper() in self.lsPalabra:
            for i in range(len(self.lsPalabra)):
                if self.lsPalabra[i].upper() == str(pl).upper():
                    self.lsAdivina[i] = self.lsPalabra[i]
        else:
            return False
        return True

        
    def getPalabra(self) -> list:
        """getPalabra()

        Returns:
            list: Retorna lista de la palabra seleccionada.
        """
        return self.lsPalabra

    def getAdivina(self) -> list:
        """getAdivina()

        Returns:
            list: Retorna lista con las palabras acertadas.
        """
        return self.lsAdivina

    def igualaListas(self) -> bool:
        """igualaListas()

        Returns:
            bool: Regresa True si las listas lsPalabra y lsAdivina son iguales.
        """
        return ("".join(self.getAdivina()) == "".join(self.getPalabra()))
    
    def existePalabra(self, pl) -> bool:
        """existePalabra()

        Args:
            pl (string): Es la palabra que ingresa el usuario.

        Returns:
            bool: Regresa True si pl ya existe en lsAdivina.
        """
        return (str(pl).lower() in self.lsAdivina or str(pl).upper() in self.lsAdivina)