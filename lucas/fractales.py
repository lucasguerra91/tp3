import os
import logica as l
import sys


def main():
    """

    """
    try:
        if not len(sys.argv) == 4:
            raise IndexError

        if os.path.isfile(sys.argv[1]):
            archivo = sys.argv[1]
        else:
            raise FileExistsError

        if int(sys.argv[2]) > 0:
            cantidad = int(sys.argv[2])
        else:
            raise TypeError

        if str(sys.argv[3]).lower().endswith('.svg'):
            destino = str(sys.argv[3]).lower()
        else:
            raise ValueError

        angulo, axioma, traducciones = l.cargar_archivo(archivo)
        secuencia_comandos = l.traducir(axioma, traducciones, cantidad)

        l.crear_svg(destino, secuencia_comandos, angulo)
        print(f'Se creó con éxito el archivo {destino} a partir del fractal {archivo}.\n Hasta luego..')
    except IndexError:
        print(f"La cantidad de argumentos no es la correcta.")
    except FileExistsError:
        print(f"El archivo de origen ingresado no existe, reviselo e intete nuevamente.")
    except TypeError:
        print(f"La cantidad ingresada debe ser un numero positivo")
    except ValueError:
        print(f"La extensión del archivo de destino debe ser .svg")


# ejecucion
main()
os.system('pause')
