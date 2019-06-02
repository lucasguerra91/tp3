from tortuga import *
from pluma import *
from pila import *


def procesador(archivo):
	try:
		with open(archivo) as archivo:
			angulo = float(archivo.readline().rstrip('\n'))
			axioma = archivo.readline().rstrip('\n')

			reglas = {}

			for linea in archivo:
				precesor, sucesor = linea.rstrip('\n').split()
				reglas[precesor] = sucesor

	except IOError:
		print(f'No se encontró {archivo}.')
		return

	except ValueError:
		print('Ángulo inválido.')
		return

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
	pila_tortugas.apilar(Tortuga(0, 0, 0, Pluma()))
	tortuga_activa = pila_tortugas.ver_tope()

	try:
		with open(nombre_imagen, 'w') as imagen:
			imagen.write(
				f'<svg viewBox="-100 -100 200 200" xmlns="http://www.w3.org/2000/svg">\n')

			longitud = len(sistema)

			i = 0

			while i < longitud:

				caracter = sistema[i]

				if caracter in ('F', 'G'):

					pasos = iterador(sistema, i, longitud, ('F', 'G'))

					i += pasos-1

					imagen.write(armar_linea(
						modulo_FG(tortuga_activa, pasos), tortuga_activa))

				elif caracter in ('f', 'g'):

					pasos = iterador(sistema, i, longitud, ('f', 'g'))

					i += pasos-1

					imagen.write(armar_linea(
						modulo_fg(tortuga_activa, pasos), tortuga_activa))

				elif caracter == '+':
					tortuga_activa.derecha(angulo)

				elif caracter == '-':
					tortuga_activa.izquierda(angulo)

				elif caracter == '|':
					tortuga_activa.izquierda(180)

				elif caracter == '[':
					pila_tortugas.apilar(tortuga_activa.clonar())

				elif caracter == ']':
					pila_tortugas.desapilar()

				i += 1

			imagen.write('</svg>')
	except IOError:
		print(f"No se encontró {nombre_imagen}.")


def armar_linea(posiciones, tortuga):

	pluma = tortuga.devolver_pluma()
	ancho = pluma.devolver_ancho()
	color = pluma.devolver_color()

	posicion_inicial,posicion_final = posiciones
	x1, y1 = posicion_inicial
	x2, y2 = posicion_final

	linea = f'<line x1="{x1}" y1="{-y1}" x2="{x2}" y2="{-y2}" stroke-width="{ancho}" stroke="{color}"/>\n'
	return linea


def iterador(sistema, i, longitud, tupla):
	pasos = 1

	while i < longitud - 1:
		siguiente = sistema[i+pasos]

		if siguiente not in tupla:
			break

		pasos += 1

	return pasos


def modulo_FG(tortuga,pasos):
	posicion_inicial = tortuga.ubicacion()
	tortuga.adelante(pasos)
	posicion_final = tortuga.ubicacion()

	return posicion_inicial, posicion_final


def modulo_fg(tortuga,pasos):
	tortuga_activa.pluma_arriba()
	posicion_inicial = tortuga.ubicacion()
	tortuga_activa.adelante(pasos)
	posicion_final = tortuga.ubicacion()
	tortuga_activa.pluma_abajo()

	return posicion_inicial, posicion_final
