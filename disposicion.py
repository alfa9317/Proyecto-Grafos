import pygame
import random
from math import log, atan2, cos, sin

params = [1.6, 0.8, 0.4, 0.8]

dimensiones = {"ancho": 800, "alto": 600, "borde": 20}
pantalla = pygame.display.set_mode((dimensiones["ancho"], dimensiones["alto"]))

colores = {"fondo": (223, 246, 255), "nodo": (71, 181, 255), "bordeNodo": (19, 99, 223), "aristas": (6, 40, 61)}

especificaciones = {"iteraciones": 2000, "fps": 30, "radioNodo": 8,
                    "minDis": min(dimensiones["ancho"], dimensiones["alto"]), "anchoNodoMin": 16,
                    "alturaNodoMin": 16, "anchoNodoMax": dimensiones["ancho"] - 16, "alturaNodoMax": dimensiones["alto"] - 16}

def dibujar(g):
    dibujarAristas(g)
    dibujarNodos(g)
    pygame.display.update()


def spring(g):

    inicializar(g)
    dibujar(g)

    reloj = pygame.time.Clock()

    cont = 0

    while True:
        reloj.tick(especificaciones["fps"])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return False
        if cont > especificaciones["iteraciones"]:
            continue

        pantalla.fill(colores["fondo"])

        actualizar(g)
        dibujar(g)

        cont += 1

    pygame.quit()


def fruchterman_reginold(g):
    reloj = pygame.time.Clock()

    inicializar(g)
    dibujar(g)

    checker = True

    while checker:

        reloj.tick(especificaciones["fps"])

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                checker = False

        pantalla.fill(colores["fondo"])
        actualizar(g)
        dibujar(g)

    pygame.quit()

def inicializar(g):

    for node in g.nodos.values():

        x = random.randrange(especificaciones["anchoNodoMin"], especificaciones["anchoNodoMax"])
        y = random.randrange(especificaciones["alturaNodoMin"], especificaciones["alturaNodoMax"])

        node.atributos['coordenadas'] = [x, y]

    return

def actualizar(g):
    for n in g.nodos.values():

        aX = 0
        aY = 0

        n1X = n.atributos['coordenadas'][0]
        n1Y = n.atributos['coordenadas'][1]

        for ns in n.enlace:

            n2X = g.nodos[ns].atributos['coordenadas'][0]
            n2Y = g.nodos[ns].atributos['coordenadas'][1]

            d = ((n1X - n2X) ** 2 + (n1Y - n2Y)**2) ** 0.5

            if d < especificaciones["minDis"]:
                continue

            atraccion = params[0] * log(d / params[1])

            aX += atraccion * cos(atan2(n2Y - n1Y, n2X - n1X))
            aY += atraccion * sin(atan2(n2Y - n1Y, n2X - n1X))

        sinConeccion = (ns for ns in g.nodos.values()
                         if (ns.id not in n.enlace and ns != n))

        rX = 0
        rY = 0

        for ns in sinConeccion:
            n2X, n2Y = ns.atributos['coordenadas']

            d = ((n1X - n2X) ** 2 + (n1Y - n2Y)**2) ** 0.5

            if d == 0:
                continue

            repulsion = params[2] / d ** 0.5

            rX -= repulsion * cos(atan2(n2Y - n1Y, n2X - n1X))
            rY -= repulsion * sin(atan2(n2Y - n1Y, n2X - n1X))

        fx = aX + rX
        fy = aY + rY

        n.atributos['coordenadas'][0] += params[3] * fx
        n.atributos['coordenadas'][1] += params[3] * fy

        n.atributos['coordenadas'][0] = max(n.atributos['coordenadas'][0], especificaciones["anchoNodoMin"])
        n.atributos['coordenadas'][1] = max(n.atributos['coordenadas'][1], especificaciones["alturaNodoMin"])
        n.atributos['coordenadas'][0] = min(n.atributos['coordenadas'][0], especificaciones["anchoNodoMax"])
        n.atributos['coordenadas'][1] = min(n.atributos['coordenadas'][1], especificaciones["alturaNodoMax"])



def dibujarNodos(g):

    for node in g.nodos.values():

        pygame.draw.circle(pantalla, colores["nodo"], node.atributos['coordenadas'], especificaciones["radioNodo"])
        pygame.draw.circle(pantalla, colores["bordeNodo"], node.atributos['coordenadas'], especificaciones["radioNodo"], 4)



def dibujarAristas(g):

    for edge in g.aristas:

        n1 = edge[0]
        n2 = edge[1]

        u = g.nodos[n1].atributos['coordenadas']
        v = g.nodos[n2].atributos['coordenadas']

        pygame.draw.line(pantalla, colores["aristas"], u, v, 2)
