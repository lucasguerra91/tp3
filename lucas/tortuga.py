import math


class Tortuga:
    """

    """

    def __init__(self, x, y, orientacion, pluma):
        self.x = x
        self.y = y
        self.pluma = pluma
        self.orientacion = orientacion

    # Getters and setters

    def ubicacion(self):
        return self.x, self.y

    def orientacion(self):
        return self.orientacion

    def pluma(self):
        return self.pluma

    # Metodos

    def pluma_abajo(self):
        self.pluma = True

    def pluma_arriba(self):
        self.pluma = False

    def girar_derecha(self, angulo):
        self.orientacion = (self.orientacion + angulo) % 360

    def girar_izquierda(self, angulo):
        self.orientacion = (self.orientacion - angulo) % 360

    def avanzar(self, unidad, destino):
        x, y = self.ubicacion()

        self.x = self.x + unidad * round(math.cos(math.radians(self.orientacion)), 2)
        self.y = self.y + unidad * round(math.sin(math.radians(self.orientacion)), 2)

        if self.pluma:
            destino.write(f'\t<line x1="{x}" y1="{y}" x2="{self.x}" y2="{self.y}" stroke-width="1" stroke="black" />\n')

    def clonar(self):
        nueva_tortuga = Tortuga(self.x, self.y, self.orientacion, self.pluma)
        return nueva_tortuga
