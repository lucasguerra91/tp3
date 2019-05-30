import os
import logica as l

def main(archivo, cantidad):
    """

    :return:
    """
    angulo, axioma, traducciones = l.cargar_archivo(archivo)
    secuencia_comandos = l.traducir(axioma, traducciones, cantidad)

    l.dibujar_con_tortuga(secuencia_comandos, angulo)


# ejecucion
main('arbol1.sl', 6)
os.system('pause')

