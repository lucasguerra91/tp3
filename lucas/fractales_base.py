import os
import logica as l


def main(archivo, cantidad, destino):
    """

    :return:
    """
    angulo, axioma, traducciones = l.cargar_archivo(archivo)
    secuencia_comandos = l.traducir(axioma, traducciones, cantidad)
    # print(secuencia_comandos)

    # l.dibujar_con_tortuga(secuencia_comandos, angulo)
    l.crear_svg(destino, secuencia_comandos, angulo)


# ejecucion
main('ejemplo.sl', 6, 'test.svg')

# os.system('pause')
