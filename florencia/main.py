import sys
from funciones import procesador, generador_sistema, dibujar

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

    except:
        print('Cantidad iteraciones inválida')
        return

    try:
        angulo, axioma, reglas = procesador(archivo)

    except:
        return

    sistema = generador_sistema(axioma, reglas, iteraciones)
    dibujar(angulo, sistema, nombre_imagen)
    print('Imagen lista.')


main()
