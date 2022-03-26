import random
from algoritmos import gMalla, gErdRen, gGilbert, gGeografico, gBarabasiAlbert, gDorogovtsevMendes


def main():
    path = ("Proyecto1_JATG_")

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

        graf = gMalla(*(malla_a, malla_b))
        graf.aGraphviz(path + graf.id + ".gv")

        graf = gErdRen(nodos, erdren)
        graf.aGraphviz(path + graf.id + ".gv")

        graf = gGilbert(nodos, gilbert, dirigido=False, auto=False)
        graf.aGraphviz(path + graf.id + ".gv")

        graf = gGeografico(nodos, geografico)
        graf.aGraphviz(path + graf.id + ".gv")

        graf = gBarabasiAlbert(nodos, barabasi_albert, auto=False)
        graf.aGraphviz(path + graf.id + ".gv")

        graf = gDorogovtsevMendes(nodos, dirigido=False)
        graf.aGraphviz(path + graf.id + ".gv")

if __name__ == "__main__":
        main()