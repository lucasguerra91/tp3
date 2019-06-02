import sys
from funciones import procesador, generador_sistema, dibujar

COMANDO = sys.argv


def main():
    if len(COMANDO) != 4:
        print('Comando inválido.')

    _, archivo, iteraciones, nombre_imagen = COMANDO

    try:
        iteraciones = int(iteraciones)

    except:
        print('Cantidad iteraciones inválida')
        return

    angulo, axioma, reglas = procesador(archivo)
    sistema = generador_sistema(axioma, reglas, iteraciones)
    dibujar(angulo, sistema, nombre_imagen)
    print('Imagen lista.')


main()
