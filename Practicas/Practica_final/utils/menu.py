class Menu:
    def __init__(self):
        """__init__()
        Constructor de la clase Menu.
        """
        self.caracter = "*"

    def encabezado(self,size):
        """encabezado()

        Args:
            size (int): Recibe el tamaño de caracteres que contiene el titulo del juego.

        Returns:
            str: Devuelve una cadena * dependiendo de longitud del titulo.
        """
        head = ""
        for i in range(size):
            head = head + self.caracter
        return head

    def opts(self,titulo, *opt, **mensajes):
        """opts()

        Args:
            titulo (str): Recibe el tutulo del menu, las opciones a mostrar y sus opciones de error.

        Returns:
            int: Retorna la opción seleccionada por el usuario.
        """
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