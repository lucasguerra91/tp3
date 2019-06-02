import sys
from funciones import procesador, sistema, dibujar

_, ARCHIVO, ITERACIONES, NOMBRE_IMAGEN = sys.argv


def main():
    angulo, axioma, reglas = procesador(ARCHIVO)
    sistema(axioma, reglas, int(ITERACIONES))
    dibujar(angulo, sistema, NOMBRE_IMAGEN)

    print('Imagen lista.')


main()
