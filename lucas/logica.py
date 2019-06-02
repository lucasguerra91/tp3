import tortuga as t
import pila as p


def cargar_archivo(archivo):
    """
    Recibe el archivo del fractal, devuelve el angulo, axioma y lista de traducciones
    """

    with open(archivo, 'r')as f:
        angulo = float(f.readline())
        axioma = f.readline().rstrip('\n')
        traducciones = {}

        for linea in f:
            clave, valor = linea.split()
            traducciones[clave] = traducciones.get(clave, valor)

    return angulo, axioma, traducciones


def traducir(axioma, traducciones, cantidad):
    """

    :param axioma:  cadena que define el estado inicial
    :param traducciones: lista de traducciones predecesor - sucesor
    :return: secuencia traducida
    """
    secuencia = ''
    while cantidad > 0:
        for c in axioma:
            secuencia += traducciones.get(c, c)
        return traducir(secuencia, traducciones, cantidad - 1)
    return axioma


def crear_svg(destino, secuencia, angulo):
    """
    Recibe como parametros el archivo .svg de destino, la secuencia de comandos
    y el angulo de giro.
    Pre-condiciones: la secuencia de comandos debe haber sido generada previamente
    a partir de un axioma y un diccionario de traducciones.
    Post: Se genera el archivo .svg indicado contiendo las etiquetas xml generadas
    a partir de dibujar la secuencia de comandos utilizando la clase tortuga.
    """
    unidad = 3
    with open(destino, 'w') as f:

        f.write('<svg viewBox="-400 -500 800 600" xmlns="http://www.w3.org/2000/svg">\n')

        tortuguero = p.Pila()
        tortuguero.apilar(t.Tortuga(0, 0, 270, True))

        dibujar(secuencia, tortuguero, unidad, angulo, f)

        f.write('</svg>\n')


def dibujar(secuencia, tortuguero, unidad, angulo, f):
    """
    Recibe una secuencia de comandos, una pila de tortugas, una unidad , un angulo
    y el archivo en el cual se debe escribir.
    La funcion escribe directamente sobre el archivo los comandos incluidos en la
    secuencia. 
    """
    for c in secuencia:
        if c == 'F' or c == 'G':
            tortuguero.ver_tope().avanzar(unidad, f)

        if c == 'f' or c == 'g':
            tortuguero.ver_tope().pluma_arriba()
            tortuguero.ver_tope().avanzar(unidad)
            tortuguero.ver_tope().pluma_abajo()

        if c == '+':
            tortuguero.ver_tope().girar_derecha(angulo)

        if c == '-':
            tortuguero.ver_tope().girar_izquierda(angulo)

        if c == '|':
            tortuguero.ver_tope().girar_derecha(180)

        if c == '[':
            tortuguero.apilar(tortuguero.ver_tope().clonar())

        if c == ']':
            tortuguero.desapilar()

        if c == 'a':
            tortuguero.ver_tope().pluma.cambiar_color('blue')

        if c == 'b':
            tortuguero.ver_tope().pluma.cambiar_color('red')

        if c == '1':
            tortuguero.ver_tope().pluma.cambiar_ancho(1)

        if c == 'a':
            tortuguero.ver_tope().pluma.cambiar_ancho(2)

        if c == 'L':
            tortuguero.ver_tope().circulo(unidad, f)
