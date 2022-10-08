class Menu:
    def __init__(self):
        self.caracter = "*"

    def encabezado(self,size):
        head = ""
        for i in range(size):
            head = head + self.caracter
        return head

    def opts(self,titulo, *opt, **mensajes):
        mensajes.setdefault("primera_vez", True)
        mensajes.setdefault("error", "Opcion no existe")
        if mensajes["primera_vez"]:
            titulo = ":::::::: BIENVENIDO al " + titulo + " ::::::::"
            print(self.encabezado(len(titulo)))
            print(titulo)
            print(self.encabezado(len(titulo)))
        else:
            titulo = ":::::::: " + titulo + " ::::::::"
            print(self.encabezado(len(titulo)))
            print(titulo)
            print(self.encabezado(len(titulo)))

        for i in range(len(opt)):
            print(f"{i+1}.- {opt[i]}")
        opc = int(input("Selecciona una opción:  "))
        if opc >= 1 and opc <= len(opt):
            return opc
        else:
            print(mensajes["error"])
            return -1