class Pluma:
	'''Crea una Pluma para ser utilizada por la clase Tortuga.'''

	def __init__(self, ancho=1, color="black"):
		self.ancho = ancho
		self.color = color
		self.abajo = True

	def esta_abajo(self):
		'''Devuelve la posición de la Pluma:
		   True si está abajo, False si está arriba.'''
		return self.abajo

	def pluma_arriba(self):
		'''Cambia la posición de la Pluma a "arriba".'''
		self.abajo = False

	def pluma_abajo(self):
		'''Cambia la posición de la Pluma a "abajo".'''
		self.abajo = True

	def cambiar_ancho(self, ancho):
		'''Cambia el ancho de la Pluma.'''
		self.ancho = ancho

	def cambiar_color(self, color):
		'''Cambia el color de la Pluma.'''
		self.color = color

	def obtener_ancho(self):
		'''Devuelve el ancho de la Pluma.'''
		return self.ancho

	def obtener_color(self):
		'''Devuelve el color de la Pluma.'''
		return self.color

	def copiar(self):
		'''Crea una nueva instancia de Pluma, con los mismos atributos.'''
		return Pluma(self.ancho, self.color)
