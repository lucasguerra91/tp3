from tortuga import *
from pluma import *
from pila import *


def procesador(archivo):
	try:
		with open(archivo) as archivo:
			try:
				angulo = float(archivo.readline().rstrip('\n'))
			
			except ValueError:
				archivo_inválido()
		
			axioma = archivo.readline().rstrip('\n')

			if not axioma:
				archivo_inválido()

			reglas = {}

			for linea in archivo:

				try:
					precesor, sucesor = linea.rstrip('\n').split()
					reglas[precesor] = sucesor

				except ValueError:
					archivo_inválido()

			if not reglas:
				archivo_inválido()
	
	except IOError:
		print(f'No se encontró {archivo}.')
		raise IOError

	return angulo, axioma, reglas


def generador_sistema(axioma, reglas, n):
	if n == 1:
		return axioma

	cadena_final = ""

	for c in axioma:
		cadena_final += reglas.get(c, c)

	return generador_sistema(cadena_final, reglas, n-1)


def dibujar(angulo, sistema, nombre_imagen):
	pila_tortugas = Pila()
	pila_tortugas.apilar(Tortuga(0, 0, 270, Pluma()))
	tortuga_activa = pila_tortugas.ver_tope()

	with open(nombre_imagen, 'w') as imagen:
		imagen.write(
			f'<svg viewBox="-400 -500 800 600" xmlns="http://www.w3.org/2000/svg">\n')

		for c in sistema:

			if c in ('F','G'):
				posicion_inicial = tortuga_activa.ubicacion()
				tortuga_activa.adelante(3)
				posicion_final = tortuga_activa.ubicacion()
				linea = armar_linea(posicion_inicial,posicion_final,tortuga_activa)
				imagen.write(linea)

			elif c in ('f','g'):

				tortuga_activa.pluma_arriba()
				tortuga_activa.adelante(3)
				tortuga_activa.pluma_abajo()

			elif c == '+':
				tortuga_activa.derecha(angulo)

			elif c == '-':
				tortuga_activa.izquierda(angulo)
				
			elif c == '|':
				tortuga_activa.izquierda(180)

			elif c == '[':
				pila_tortugas.apilar(tortuga_activa.clonar())

			elif c == ']':
				pila_tortugas.desapilar()

		imagen.write('</svg>')


def armar_linea(p1,p2,tortuga):

	pluma = tortuga.devolver_pluma()
	ancho = pluma.devolver_ancho()
	color = pluma.devolver_color()

	x1, y1 = p1
	x2, y2 = p2

	linea = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="{ancho}" stroke="{color}"/>\n'
	return linea

def archivo_inválido():
	print("Archivo de instrucciones inválido.")
	print('''
Ejemplo de un archivo válido:

27.2
X
X X-F+G
F FG+

Donde la primera línea es el ángulo, la segunda el axioma y las siguientes líneas \
las reglas de cambio, con los símbolos separados de su traducción por un espacio.''')
	raise ValueError