class Pluma:
    def __init__(self, ancho=1, color="black"):
        self.ancho = ancho
        self.color = color
        self.abajo = False

    def esta_abajo(self):
        return self.abajo

    def pluma_arriba(self):
        self.abajo = False

    def pluma_abajo(self):
        self.abajo = True

    def cambiar_ancho(self, ancho):
        self.ancho = ancho

    def cambiar_color(self, color):
        self.color = color

    def get_ancho(self):
        return self.ancho

    def get_color(self):
        return self.color

    def copiar(self):
        return Pluma(self.ancho, self.color)
