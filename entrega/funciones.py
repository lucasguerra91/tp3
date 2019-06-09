import tortuga as t
import pila as pi
import pluma as p

def procesador(archivo):
	"""Recibe el archivo del fractal, devuelve el angulo, axioma y diccionario de reglas"""
	with open(archivo) as archivo:

		angulo = float(archivo.readline().rstrip('\n'))
		axioma = archivo.readline().rstrip('\n')

		if not axioma:
			raise ValueError

		reglas = {}

		for linea in archivo:

			precesor, sucesor = linea.rstrip('\n').split()
			reglas[precesor] = sucesor

		if not reglas:
			raise ValueError

	return angulo, axioma, reglas


def generador_sistema(axioma, reglas, n):
	"""
	Genera el sistema a partir de un axioma, diccionario de reglas y la cantidad
	de veces que deben aplicarse las mismas.
	:param axioma:  cadena que define el estado inicial
	:param regals: lista de traducciones predecesor - sucesor
	:return: sistema L traducida
	"""
	if n == 1:
		return axioma

	cadena_final = ""

	for c in axioma:
		cadena_final += reglas.get(c, c)

	return generador_sistema(cadena_final, reglas, n - 1)


def crear_svg(destino, sistema, angulo, iteraciones):
	"""
	Recibe como parametros el archivo .svg de destino, el sistema de comandos
	y el angulo de giro.
	Pre-condiciones: el sistema debe haber sido generada previamente
	a partir de un axioma y un diccionario de traducciones.
	Post: Se genera el archivo .svg indicado contiendo las etiquetas xml generadas
	a partir de dibujar la secuencia de comandos utilizando la clase tortuga.
	"""
	unidad = 3
	with open(destino, 'w') as f:

		f.write(
			f'<svg viewBox="-500 -500 1024 768" xmlns="http://www.w3.org/2000/svg">\n')
		tortuguero = pi.Pila()
		tortuguero.apilar(t.Tortuga(0, 0, 270, p.Pluma()))

		dibujar(sistema, tortuguero, unidad, angulo, f)

		f.write('</svg>\n')


def dibujar(secuencia, tortuguero, unidad, angulo, f):
	"""
	Recibe una secuencia de comandos, una pila de tortugas, una unidad , un angulo
	y el archivo en el cual se debe escribir.
	La funcion escribe directamente sobre el archivo los comandos incluidos en la
	secuencia.
	"""
	for c in secuencia:
		if c == 'F' or c == 'G':
			tortuguero.ver_tope().avanzar(unidad, f)

		elif c == 'f' or c == 'g':
			tortuguero.ver_tope().pluma.pluma_arriba()
			tortuguero.ver_tope().avanzar(unidad, f)
			tortuguero.ver_tope().pluma.pluma_abajo()

		elif c == '+':
			tortuguero.ver_tope().girar_derecha(angulo)

		elif c == '-':
			tortuguero.ver_tope().girar_izquierda(angulo)

		elif c == '|':
			tortuguero.ver_tope().girar_derecha(180)

		elif c == '[':
			tortuguero.apilar(tortuguero.ver_tope().clonar())

		elif c == ']':
			tortuguero.desapilar()

		elif c == 'a':
			tortuguero.ver_tope().obtener_pluma().cambiar_color('blue')

		elif c == 'b':
			tortuguero.ver_tope().obtener_pluma().cambiar_color('red')

		elif c == '1':
			tortuguero.ver_tope().obtener_pluma().cambiar_ancho(1)

		elif c == 'a':
			tortuguero.ver_tope().obtener_pluma().cambiar_ancho(2)

		elif c == 'L':
			tortuguero.ver_tope().circulo(unidad, f)
