class Pila:
    """Representa una pila con operaciones de apilar, desapilar y
    verifica si esta vacia """

    def __init__(self):
        """ Crea una pila vacia """
        self.items = []

    def esta_vacia(self):
        """ Devuelve True si la lista esta vacia, False si no.. """
        return len(self.items) == 0

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila esta vacia levanta una excepcion """
        if self.esta_vacia():
            raise IndexError("La pila está vacía.")
        return self.items.pop()

    def ver_tope(self):
        """ Devuelve el elemento tope """
        return self.items[len(self.items)-1]

