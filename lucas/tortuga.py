import math


class Tortuga:
    """
    Modela una clase Tortuga similar al modulo turtle de python
    """

    def __init__(self, x, y, orientacion, pluma):
        self.x = x
        self.y = y
        self.pluma = pluma
        self.orientacion = orientacion

    # Getters and setters

    def ubicacion(self):
        """ Devuelve las coordenadas de la ubicacion actual de la Tortuga ."""
        return self.x, self.y

    def orientacion(self):
        """ Devuelve el angulode la orientacion actual de la Tortuga ."""
        return self.orientacion

    def pluma(self):
        """ Devuelve el estado actual de la pluma de la Tortuga ."""
        return self.pluma

    def pluma_abajo(self):
        """ Cambia el estado de la pluma hacia abajo (True - escribir)"""
        self.pluma = True

    def pluma_arriba(self):
        """ Cambia el estado de la pluma hacia ariiba (False - no escribir)"""
        self.pluma = False

    # Metodos

    def girar_derecha(self, angulo):
        self.orientacion = (self.orientacion + angulo) % 360

    def girar_izquierda(self, angulo):
        self.orientacion = (self.orientacion - angulo) % 360

    def avanzar(self, unidad, destino):
        """Recibe una unidad (cuanto debe avanzar), y el nombre del archivo en
        el cual escribir.
        Actualiza la ubicacion de la tortuga y escribe en el archivo de destino
        si la pluma esta abajo-"""
        x, y = self.ubicacion()

        self.x = self.x + unidad * round(math.cos(math.radians(self.orientacion)), 2)
        self.y = self.y + unidad * round(math.sin(math.radians(self.orientacion)), 2)

        if self.pluma:
            destino.write(f'\t<line x1="{x}" y1="{y}" x2="{self.x}" y2="{self.y}" stroke-width="1" stroke="black" />\n')

    def clonar(self):
        return Tortuga(self.x, self.y, self.orientacion, self.pluma)
