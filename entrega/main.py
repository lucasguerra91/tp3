import sys
import funciones as f

COMANDO = sys.argv


def main():
	if len(COMANDO) != 4:
		print('Comando inválido.')
		return

	_, archivo, iteraciones, nombre_imagen = COMANDO

	if nombre_imagen[-4:] != ".svg":
		nombre_imagen += ".svg"

	try:
		iteraciones = int(iteraciones)

		if not iteraciones > 0:
			raise ValueError

	except:
		print('Cantidad de iteraciones inválida.')
		return

	try:
		angulo, axioma, reglas = f.procesador(archivo)

	except:
		return

	sistema = f.generador_sistema(axioma, reglas, iteraciones)
	f.crear_svg(nombre_imagen, sistema, angulo, iteraciones)
	print(f'Imagen lista.\nSe generó {nombre_imagen}')


main()
