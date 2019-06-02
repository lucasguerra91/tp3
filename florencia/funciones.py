import tortuga
import pluma
import pila


def procesador(archivo):

    with open(archivo) as archivo:
        angulo = float(archivo.readline().rstrip('\n'))
        axioma = archivo.readline().rstrip('\n')

        reglas = {}

        for linea in archivo:
            precesor, sucesor = linea.rstrip('\n').split()
            reglas[precesor] = sucesor

    return angulo, axioma, reglas


def sistema(axioma, reglas, n):
    if n == 1:
        return axioma

    cadena_final = ""

    for c in axioma:
        cadena_final += reglas.get(c, c)

    return sistema(cadena_final, reglas, n-1)


def dibujar(angulo, sistema, nombre_imagen):
    pila_tortugas = Pila()
    pila_tortugas.apilar(Tortuga(0, 0, 0, Pluma()))
    tortuga_activa = pila_tortugas.ver_tope()

    with open(nombre_imagen, 'w') as imagen:
        imagen.write(
            f'<svg viewBox="-100 -100 200 200" xmlns="http://www.w3.org/2000/svg">\n')

        longitud = len(sistema)

        i = 0

        while i < longitud:

            caracter = sistema[i]

            if caracter in ('F', 'G'):
                pasos = 1

                while i < longitud - 1:
                    siguiente = sistema[i+pasos]

                    if siguiente not in ('F', 'G'):
                        break

                    pasos += 1

                i += pasos-1

                tortuga_activa.adelante(pasos)

            elif caracter in ('f', 'g'):
                pasos = 1

                while i < longitud - 1:
                    siguiente = sistema[i+1]

                    if siguiente not in ('f', 'g'):
                        break

                    pasos += 1

                i += pasos-1

                tortuga_activa.pluma_arriba()
                tortuga_activa.adelante(pasos)
                tortuga_activa.pluma_abajo()

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
