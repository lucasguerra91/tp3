import sys
import funciones as f

COMANDO = sys.argv


def main():
	'''
	El programa recibe por comando de consola:
	1) Un archivo con un ángulo y un sistema de Lindenmayer.
	2) Una cantidad de iteraciones.
	3) El nombre del archivo svg a generar.
	A partir de las instrucciones del archivo genera una imagen fractal en formato svg. 
	'''

	if len(COMANDO) != 4:
		print('Comando inválido.')
		return

	_, archivo, iteraciones, nombre_imagen = COMANDO

	if nombre_imagen[-4:] != ".svg":
		nombre_imagen += ".svg"

	try:
		iteraciones = int(iteraciones)

		if not iteraciones > 0:
			print('Cantidad de iteraciones inválida.')
			return

	except:
		print('Cantidad de iteraciones inválida.')
		return

	try:
		angulo, axioma, reglas = f.procesador(archivo)

	except IOError:
		print(f'No se encontró {archivo}.')
		return

	except:
		print("Archivo de instrucciones inválido.")
		print("\nEjemplo de un archivo válido:\n\n27.2\nX\nX X-F+G\nF FG+\n")
		print("Donde la primera línea es el ángulo, la segunda el axioma y las siguientes líneas \
las reglas de cambio, con los símbolos separados de su traducción por un espacio.")
		return

	sistema = f.generador_sistema(axioma, reglas, iteraciones)
	f.crear_svg(nombre_imagen, sistema, angulo, iteraciones)
	print(f'Imagen lista.\nSe generó {nombre_imagen}')


main()
