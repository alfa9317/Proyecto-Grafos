import random
import sys


from grafo import Grafo
from arista import Arista
from nodo import Nodo


def verification(type, x, y):
    match type:
        case 0:
             if y < 2 or x < 2:
                print("No se cumple con n > 1 y m > 1", file=sys.stderr)
                exit(-1)
        case 1:
            if y < x - 1 or x < 1:
                print("No se cumple con los requerimientos de n > 0 y m >=  (n - 1)", file=sys.stderr)
                exit(-1)
        case 2:
            if y > 1 or y < 0 or x < 1:
                print(" No se cumple con n > 0 y 0 <= p <= 1", file=sys.stderr)
                exit(-1)
        case 3:
            if y > 1 or y < 0 or x < 1:
                print("No se cumple con n > 0 y 0 <= r <= 1", file=sys.stderr)
                exit(-1)
        case 4:
            if x < 1 or y < 2:
                print("No se cumple con n > 0 y d > 1", file=sys.stderr)
                exit(-1)
        case 5:
            if x < 3:
                print("No se cumple con n >= 3", file=sys.stderr)
                exit(-1)


def gMalla(n, m, dirigido=False):
    verification(0, n, m)

    totalN = m * n
    graf = Grafo(id=f"Grafo de Malla. Nodos: {n} Aristas:{m}", dirigido=dirigido)
    nodos = graf.nodos

    for nodo in range(totalN):
        graf.agregarNodo(Nodo(nodo))

    graf.agregarArista(Arista(nodos[0], nodos[1]))
    graf.agregarArista(Arista(nodos[0], nodos[m]))

    for i in range(1, m - 1):
        graf.agregarArista(Arista(nodos[i], nodos[i - 1]))
        graf.agregarArista(Arista(nodos[i], nodos[i + 1]))
        graf.agregarArista(Arista(nodos[i], nodos[i + m]))

    graf.agregarArista(Arista(nodos[m - 1], nodos[m - 2]))
    graf.agregarArista(Arista(nodos[m - 1], nodos[m - 1 + m]))

    for i in range(m, totalN - m):
        col = i % m
        graf.agregarArista(Arista(nodos[i], nodos[i - m]))
        graf.agregarArista(Arista(nodos[i], nodos[i + m]))
        if col == 0:
            graf.agregarArista(Arista(nodos[i], nodos[i + 1]))
        elif col == (m-1):
            graf.agregarArista(Arista(nodos[i], nodos[i - 1]))
        else:
            graf.agregarArista(Arista(nodos[i], nodos[i + 1]))
            graf.agregarArista(Arista(nodos[i], nodos[i - 1]))

    col0 = totalN - m
    col1 = col0 + 1
    uNodo = totalN - 1
    graf.agregarArista(Arista(nodos[col0], nodos[col1]))
    graf.agregarArista(Arista(nodos[col0], nodos[col0 - m]))

    for i in range(col1, uNodo):
        graf.agregarArista(Arista(nodos[i], nodos[i - 1]))
        graf.agregarArista(Arista(nodos[i], nodos[i + 1]))
        graf.agregarArista(Arista(nodos[i], nodos[i - m]))

    graf.agregarArista(Arista(nodos[uNodo], nodos[uNodo - m]))
    graf.agregarArista(Arista(nodos[uNodo], nodos[uNodo - 1]))

    return graf

def dummyGraf(dirigido=True):
    graf = Grafo(id=f"Grafo. Nodos: {8} Aristas:{15}", dirigido=dirigido)
    nodos = graf.nodos
    for nodo in range(8):
        graf.agregarNodo(Nodo(nodo))

    aristas=[Arista(nodos[0], nodos[1]), Arista(nodos[0], nodos[5]), Arista(nodos[0], nodos[6]), Arista(nodos[1], nodos[2]), Arista(nodos[5], nodos[2]), Arista(nodos[5], nodos[4]), Arista(nodos[5], nodos[6]), Arista(nodos[6], nodos[4]), Arista(nodos[6], nodos[7]),
             Arista(nodos[4], nodos[3]), Arista(nodos[4], nodos[7]), Arista(nodos[3], nodos[2]), Arista(nodos[3], nodos[7]), Arista(nodos[2], nodos[4]), Arista(nodos[2], nodos[7])]

    for arista in aristas:
        graf.agregarArista(arista)

    return graf

def grafGenerator(n, maxAXNodo = 4, dirigido=False):

    graf = Grafo(id=f"Grafo Aleatorio. Nodos: {n}", dirigido=dirigido)
    nodos = graf.nodos
    rand_node = random.randrange
    for nodo in range(n):
        graf.agregarNodo(Nodo(nodo))

    for nodo in range(n):
        num_a = random.randrange(1, maxAXNodo)
        while num_a != 0:
            a = nodo
            b = rand_node(n)
            if a == b:
                continue
            graf.agregarArista(Arista(nodos[a], nodos[b]))
            num_a = num_a - 1

    return graf


def gErdRen(n, m, dirigido=False, auto=False):
    verification(1, n, m)

    graf = Grafo(id=f"Grafo de Erdos-Renyi. Nodos: {n} Aristas:{m}", dirigido=dirigido)
    nodos = graf.nodos

    for nodo in range(n):
        graf.agregarNodo(Nodo(nodo))

    rand_node = random.randrange
    for arista in range(m):
        while True:
            a = rand_node(n)
            b = rand_node(n)
            if a == b and not auto:
                continue
            if graf.agregarArista(Arista(nodos[a], nodos[b])):
                break

    return graf


def gGilbert(n, p, dirigido=False, auto=False):
    verification(2, n, p)

    graf = Grafo(id=f"Grafo Gilbert. Nodos: {n} Aristas: {int(p * 100)}", dirigido=dirigido)
    nodos = graf.nodos

    for nodo in range(n):
        graf.agregarNodo(Nodo(nodo))
    if auto:
        tuplas = ((a, b) for a in nodos.keys() for b in nodos.keys())
    else:
        tuplas = ((a, b) for a in nodos.keys() for b in nodos.keys() if a != b)

    for a, b in tuplas:
        prob = random.random()
        if prob <= p:
            graf.agregarArista(Arista(nodos[a], nodos[b]))

    return graf


def gGeografico(n, r, dirigido=False, auto=False):

    verification(3, n, r)

    coordenadas = dict()
    graf = Grafo(id=f"Grafico Geografico. Nodos: {n} Aristas: {int(r * 100)}", dirigido=dirigido)
    nodos = graf.nodos
    r **= 2

    for i in range(n):
        graf.agregarNodo(Nodo(i))
        x = round(random.random(), 3)
        y = round(random.random(), 3)
        coordenadas[i] = (x, y)

    for a in nodos:
        valores = (b for b in nodos if a != b)
        if auto:
            graf.agregarArista(Arista(nodos[a], nodos[a]))
        for b in valores:
            distNodos = (coordenadas[a][0] - coordenadas[b][0]) ** 2 \
                   + (coordenadas[a][1] - coordenadas[b][1]) ** 2
            if distNodos <= r:
                graf.agregarArista(Arista(nodos[a], nodos[b]))
    return graf


def gBarabasiAlbert(n, d, dirigido=False, auto=False):

    verification(4, n, d)

    graf = Grafo(id=f"Grafo Barabasi. Nodos:{n} Aristas:{d}", dirigido=dirigido)
    nodos = graf.nodos
    grado = dict()

    for i in range(n):
        graf.agregarNodo(Nodo(i))
        grado[i] = 0

    for i in nodos:
        for j in nodos:
            if grado[i] == d:
                break
            if grado[j] == d:
                continue
            p = random.random()
            iguales = j == i
            if iguales and not auto:
                continue

            if p <= 1 - grado[j] / d \
                    and graf.agregarArista(Arista(nodos[i], nodos[j])):
                grado[i] += 1
                if not iguales:
                    grado[j] += 1

    return graf


def gDorogovtsevMendes(n, dirigido=False):
    verification(5, n, None)

    graf = Grafo(id=f"Grafo Dorogovtsev. Nodos: {n}", dirigido=dirigido)
    nodos = graf.nodos
    aristas = graf.aristas

    for nodo in range(3):
        graf.agregarNodo(Nodo(nodo))
    pairs = ((a, b) for a in nodos for b in nodos if a != b)
    for a, b in pairs:
        graf.agregarArista(Arista(nodos[a], nodos[b]))

    for nodo in range(3, n):
        graf.agregarNodo(Nodo(nodo))
        a, b = random.choice(list(aristas.keys()))
        graf.agregarArista(Arista(nodos[nodo], nodos[a]))
        graf.agregarArista(Arista(nodos[nodo], nodos[b]))

    return graf
