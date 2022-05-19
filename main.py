import random
from nodo import Nodo
from algoritmos import gMalla, gErdRen, gGilbert, gGeografico, gBarabasiAlbert, gDorogovtsevMendes, grafGenerator, dummyGraf


def main():
    path = ("Proyecto1_JATG_")
    #----------Dijkstra---------------

    grafo = grafGenerator(5, dirigido=True)
    grafo.aGraphviz(path + grafo.id + ".gv")
    T = grafo.Dijkstra(Nodo(0))
    T.aGraphviz(path + T.id + ".gv", label=True)
    grafo = grafGenerator(10, dirigido=True)
    grafo.aGraphviz(path + grafo.id + ".gv")
    T = grafo.Dijkstra(Nodo(0))
    T.aGraphviz(path + T.id + ".gv", label=True)
    grafo = grafGenerator(20, dirigido=True)
    grafo.aGraphviz(path + grafo.id + ".gv")
    T = grafo.Dijkstra(Nodo(0))
    T.aGraphviz(path + T.id + ".gv", label=True)

    nTotal=[30, 100, 500]
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

        erdren = random.randint(nodos+1,nodos*2)
        gilbert = random.uniform(0.1,1)
        geografico = random.uniform(0.1,1)
        barabasi_albert = random.randint(1,nodos)

        #Graphs
        graf = []

        graf.append(gMalla(*(malla_a, malla_b)))
        graf.append(gErdRen(nodos, erdren))
        graf.append(gGilbert(nodos, gilbert, dirigido=False, auto=False))
        graf.append(gGeografico(nodos, geografico))
        graf.append(gBarabasiAlbert(nodos, barabasi_albert, auto=False))
        graf.append(gDorogovtsevMendes(nodos, dirigido=False))
        #graf.append(grafGenerator(nodos, dirigido=True))

        #Files
        #for g in graf:
            #g.aGraphviz(path + g.id + ".gv")

        #----------BFS-------------------
        #for g in graf:
            #T = g.BFS(Nodo(0))
            #print(T)
            #T.aGraphviz(path + T.id + ".gv")
        #----------DFS_R--------------------
        #for g in graf:
            #T = g.DFS_R(Nodo(0))
            #T.aGraphviz(path + T.id + ".gv")
        # ----------DFS_I--------------------
        #for g in graf:
            #T = g.DFS_I(Nodo(0))
            #T.aGraphviz(path + T.id + ".gv")
            #print(T.id)
        # -------------Dijkstra--------------
        #grafo = dummyGraf()
        #T = grafo.Dijkstra(Nodo(0))
        #T.aGraphviz(path + T.id + ".gv")
        grafo = grafGenerator(nodos, dirigido=True)
        grafo.aGraphviz(path + grafo.id + ".gv")
        T = grafo.Dijkstra(Nodo(0))
        T.aGraphviz(path + T.id + ".gv", label=True)

if __name__ == "__main__":
        main()
