import math
from pluma import *


class Tortuga:
    """
    Modela una clase Tortuga similar al modulo turtle de python
    """

    def __init__(self, x, y, orientacion, pluma):
        self.x = x
        self.y = y
        self.pluma = Pluma()
        self.orientacion = orientacion

    # Getters and setters

    def ubicacion(self):
        """ Devuelve las coordenadas de la ubicacion actual de la Tortuga ."""
        return self.x, self.y

    def orientacion(self):
        """ Devuelve el angulode la orientacion actual de la Tortuga ."""
        return self.orientacion

    def devolver_pluma(self):
        """ Devuelve el estado actual de la pluma de la Tortuga ."""
        return self.pluma

    def pluma_abajo(self):
        """ Cambia el estado de la pluma hacia abajo (True - escribir)"""
        self.pluma.poner_abajo()

    def pluma_arriba(self):
        """ Cambia el estado de la pluma hacia ariiba (False - no escribir)"""
        self.pluma.poner_arriba()

    # Metodos

    def derecha(self, angulo):
        """ Gira la orientacion de la tortuga a la derecha en el angulo pasado por parametro """
        self.orientacion = (self.orientacion + angulo) % 360

    def izquierda(self, angulo):
        """ Gira la orientacion de la tortuga a la izquierda en el angulo pasado por parametro """
        self.orientacion = (self.orientacion - angulo) % 360

    def adelante(self, unidad):
        """Recibe una unidad (cuanto debe avanzar), y el nombre del archivo en
        el cual escribir.
        Actualiza la ubicacion de la tortuga y escribe en el archivo de destino
        si la pluma esta abajo-"""

        x, y = self.ubicacion()

        self.x = self.x + unidad * round(math.cos(math.radians(self.orientacion)), 2)
        self.y = self.y + unidad * round(math.sin(math.radians(self.orientacion)), 2)

        
    def clonar(self):
        """Devuelve una nueva tortuga con la ubicacion, orientacion y estado de la tortuga actual. """
        return Tortuga(self.x, self.y, self.orientacion, self.pluma.copiar())