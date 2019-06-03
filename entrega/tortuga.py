import math
import pluma as p


class Tortuga:
	"""
	Modela una clase Tortuga similar al modulo turtle de python
	"""

	def __init__(self, x, y, orientacion, pluma):
		self.x = x
		self.y = y
		self.pluma = p.Pluma()
		self.orientacion = orientacion

	# Getters and setters

	def ubicacion(self):
		""" Devuelve las coordenadas de la ubicacion actual de la Tortuga ."""
		return self.x, self.y

	def orientacion(self):
		""" Devuelve el angulode la orientacion actual de la Tortuga ."""
		return self.orientacion

	# Metodos

	def girar_derecha(self, angulo):
		""" Gira la orientacion de la tortuga a la derecha en el angulo pasado por parametro """
		self.orientacion = (self.orientacion + angulo) % 360

	def girar_izquierda(self, angulo):
		""" Gira la orientacion de la tortuga a la izquierda en el angulo pasado por parametro """
		self.orientacion = (self.orientacion - angulo) % 360

	def avanzar(self, unidad, destino):
		"""Recibe una unidad (cuanto debe avanzar), y el nombre del archivo en
		el cual escribir.
		Actualiza la ubicacion de la tortuga y escribe en el archivo de destino
		si la pluma esta abajo-"""

		x, y = self.ubicacion()

		self.x = self.x + unidad * \
			round(math.cos(math.radians(self.orientacion)), 2)
		self.y = self.y + unidad * \
			round(math.sin(math.radians(self.orientacion)), 2)

		if self.pluma.esta_abajo:
			destino.write(
				f'\t<line x1="{x}" y1="{y}" x2="{self.x}" y2="{self.y}" stroke-width="{self.pluma.obtener_ancho()}" stroke="{self.pluma.obtener_color()}" />\n')

	def circulo(self, unidad, destino):
		""" Recibe una unidad y el archivo de destino. Si la pluma esta abajo,
		dibuja un circulo de centro x e y (ubicacion actual) y radio ancho de la pluma"""
		x, y = self.ubicacion()

		if self.pluma.esta_abajo:
			destino.write(
				f'\t<circle cx = "{x}" cy = "{y}" r = "{self.pluma.obtener_ancho()}" fill = "{self.pluma.obtener_color()}" />\n')

	def clonar(self):
		"""Devuelve una nueva tortuga con la ubicacion, orientacion y estado de la tortuga actual. """
		return Tortuga(self.x, self.y, self.orientacion, self.pluma.copiar())

	def obtener_pluma(self):
		'''Devuelve el atributo Pluma de la Tortuga.'''
		return self.pluma