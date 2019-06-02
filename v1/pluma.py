class Pluma:
    def __init__(self, ancho=1, color="black"):
        self.ancho = ancho
        self.color = color
        self.arriba = False

    def esta_arriba(self):
        return self.arriba

    def poner_arriba(self):
        self.arriba = True

    def poner_abajo(self):
        self.arriba = False

    def cambiar_ancho(self, ancho):
        self.ancho = ancho

    def cambiar_color(self, color):
        self.color = color

    def devolver_ancho(self):
        return self.ancho

    def devolver_color(self):
        return self.color

    def copiar(self):
        return Pluma(self.ancho, self.color)
