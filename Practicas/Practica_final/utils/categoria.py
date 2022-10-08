import random as r

class Categoria:

    dic = {
        "Nivel1" : ["Avestruz", "Ballena", "Caballo", "Elefante", "Flamenco", "Guepardo", "Hiena", "Jaguar", "Koala", "Llama", "Mapache", "Nutria", "Paloma", "Rinoceronte", "Salamandra", "Tigre", "Vaca", "Zorrillo"],
        "Nivel2" : ["Spiderman", "Logan", "Superman", "Batman", "Thor", "Deadpool"],
        "Nivel3" : ["Aguacate", "Piña", "Manzana", "Naranjas", "Guayaba", "Cereza"]
    }

    def __init__(self):
        self.palabra = ""
        self.lsPalabra = []
        self.lsAdivina = []
    

    def elijePalabra(self, nivel):
        n="Nivel"+str(nivel)
        self.palabra = Categoria.dic[n][r.randint(0,(len(Categoria.dic[n])-1))]
        self.lsPalabra = list(self.palabra)
        self.lsAdivina = ["_" for i in self.lsPalabra] 

    def actPalabra(self, pl):
        if str(pl).lower() in self.lsPalabra or str(pl).upper() in self.lsPalabra:
            for i in range(len(self.lsPalabra)):
                if self.lsPalabra[i].upper() == str(pl).upper():
                    self.lsAdivina[i] = self.lsPalabra[i]
        else:
            return False
        return True

        
    def getPalabra(self):
        return self.lsPalabra

    def getAdivina(self):
        return self.lsAdivina

    def igualaListas(self):
        return ("".join(self.getAdivina()) == "".join(self.getPalabra()))
    
    def existePalabra(self, pl):
        return (str(pl).lower() in self.lsAdivina or str(pl).upper() in self.lsAdivina)