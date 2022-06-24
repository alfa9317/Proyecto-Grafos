import random
from nodo import Nodo
from algoritmos import gMalla, gErdRen, gGilbert, gGeografico, gBarabasiAlbert, gDorogovtsevMendes, grafGenerator, dummyGraf

path = ("Proyectos_JATG_")

def mallaCall():
    print("Grafo de Malla:")
    nTotal = [30, 100, 500]
    for nodos in nTotal:
        malla_a = random.randint(2, nodos)
        malla_b = 0
        if (nodos % malla_a == 0):
            malla_b = nodos / malla_a
        else:
            while malla_b == 0:
                malla_a -= 1
                if (nodos % malla_a == 0):
                    malla_b = nodos / malla_a
        malla_a = int(malla_a)
        malla_b = int(malla_b)
        grafo = gMalla(*(malla_a, malla_b))
        grafo.aGraphviz(path + grafo.id + ".gv")

def erdosRenyiCall():
    print("Grafo Erdos-Renyi:")
    nTotal = [30, 100, 500]
    for nodos in nTotal:
        erdren = random.randint(nodos + 1, nodos * 2)
        grafo = gErdRen(nodos, erdren)
        grafo.aGraphviz(path + grafo.id + ".gv")

def gilbertCall():
    print("Grafo Gilbert:")
    nTotal = [30, 100, 500]
    for nodos in nTotal:
        gilbert = random.uniform(0.1,1)
        grafo = gGilbert(nodos, gilbert, dirigido=False, auto=False)
        grafo.aGraphviz(path + grafo.id + ".gv")

def geograficoCall():
    print("Grafo Geográfico:")
    nTotal = [30, 100, 500]
    for nodos in nTotal:
        geografico = random.uniform(0.1,1)
        grafo = gGeografico(nodos, geografico)
        grafo.aGraphviz(path + grafo.id + ".gv")

def barabasiAlbertCall():
    print("Grafo Barabási-Albert:")
    nTotal = [30, 100, 500]
    for nodos in nTotal:
        barabasi_albert = random.randint(1,nodos)
        grafo = gBarabasiAlbert(nodos, barabasi_albert, auto=False)
        grafo.aGraphviz(path + grafo.id + ".gv")

def dorogovtsevMendesCall():
    print("Grafo Dorogovtsev-Mendes:")
    nTotal = [30, 100, 500]
    for nodos in nTotal:
        grafo = gDorogovtsevMendes(nodos, dirigido=False)
        grafo.aGraphviz(path + grafo.id + ".gv")

def BFSCall():
    print("Árbol BFS:")
    nTotal = [30, 100, 500]
    for n in nTotal:
        grafo = grafGenerator(n, dirigido=True)
        T = grafo.BFS(Nodo(0))
        T.aGraphviz(path + T.id + ".gv")

def DFSRCall():
    print("Árbol DFSR:")
    nTotal = [30, 100, 500]
    for n in nTotal:
        grafo = grafGenerator(n, dirigido=True)
        T = grafo.DFS_R(Nodo(0))
        T.aGraphviz(path + T.id + ".gv")

def DFSICall():
    print("Árbol DFSI:")
    nTotal = [30, 100, 500]
    for n in nTotal:
        grafo = grafGenerator(n, dirigido=True)
        grafo.aGraphviz(path + grafo.id + ".gv")
        T = grafo.DFS_I(Nodo(0))
        T.aGraphviz(path + T.id + ".gv")
        # print(T.id)

def kruskalDCall():
    print("Árbol KruskalD:")
    nTotal = [5, 10, 20]
    grafoInf = "_usado en KruskalD"
    for n in nTotal:
        #grafo = dummyGraf()
        grafo = grafGenerator(n, dirigido=False)
        grafo.aGraphviz(path + grafo.id + grafoInf + ".gv")
        T = grafo.KruskalD()
        T.aGraphviz(path + T.id + ".gv", labela=True)

def kruskalICall():
    print("Árbol KruskalI:")
    nTotal = [5, 10, 20]
    grafoInf = "_usado en KruskalI"
    for n in nTotal:
        #grafo = dummyGraf()
        grafo = grafGenerator(n, dirigido=False)
        grafo.aGraphviz(path + grafo.id + grafoInf + ".gv")
        T = grafo.KruskalI()
        T.aGraphviz(path + T.id + ".gv", labela=True)

def primCall():
    print("Árbol Prim:")
    nTotal = [5, 10, 20]
    grafoInf = "_usado en Prim"
    for n in nTotal:
        #grafo = dummyGraf()
        grafo = grafGenerator(n, dirigido=False)
        grafo.aGraphviz(path + grafo.id + grafoInf + ".gv")
        T = grafo.Prim()
        T.aGraphviz(path + T.id + ".gv", labela=True)

def dijkstraCall():
    print("Árbol Dijkstra:")
    nTotal = [5, 10, 20]
    grafoInf = "_usado en Dijkstra"
    for n in nTotal:
        # grafo = dummyGraf()
        grafo = grafGenerator(n, dirigido=True)
        grafo.aGraphviz(path + grafo.id + grafoInf + ".gv")
        T = grafo.Dijkstra(Nodo(0))
        T.aGraphviz(path + T.id + ".gv", labeln=True)

def mainProgram():
    print("¡Bienvenido!")
    option = input("Selecciona:\n0)Salir\n1)Grafo Malla\n2)Grafo Erdos-Renyi\n3)Grafo Gilbert"
                   "\n4)Grafo Geográfico\n5)Grafo Barabási-Albert\n6)Grafo Dorogovtsev-Mendes"
                   "\n7)Árbol BFS\n8)Árbol DFSR\n9)Árbol DFSI"
                   "\n10)Árbol KruskalD\n11)Árbol KruskalI\n12)Árbol Prim"
                   "\n13)Árbol Dijkstra\n👉🏻")
    print("Seleccionaste: " + option)
    runAlgorithm(int(option))
def runAlgorithm(option = 0):
    if option == 0:
        print("¡Adios!")
    elif option == 1:
        mallaCall()
    elif option == 2:
        erdosRenyiCall()
    elif option == 3:
        gilbertCall()
    elif option == 4:
        geograficoCall()
    elif option == 5:
        barabasiAlbertCall()
    elif option == 6:
        dorogovtsevMendesCall()
    elif option == 7:
        BFSCall()
    elif option == 8:
        DFSRCall()
    elif option == 9:
        DFSICall()
    elif option == 10:
        kruskalDCall()
    elif option == 11:
        kruskalICall()
    elif option == 12:
        primCall()
    elif option == 13:
        dijkstraCall()
    else:
        print("Error: Tu selección no corresponde con las opciones")

mainProgram()
