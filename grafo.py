from arista import Arista
from nodo import Nodo
from random import randrange
import math
import time

class Grafo(object):

    def __init__(self, id='grafo', dirigido=False):
        self.id = id
        self.dirigido = dirigido
        self.nodos = dict()
        self.aristas = dict()
        self.atributos = dict()

    def __repr__(self):

        return str("id: " + str(self.id) + '\n' + 'Nodos: ' + str(self.nodos.values()) + '\n' + 'Aristas: ' + str(self.aristas.values()))

    def agregarNodo(self, nodo):

        self.nodos[nodo.id] = nodo

    def agregarArista(self, arista):

        if self.obtenerArista(arista.id):
            return False

        self.aristas[arista.id] = arista
        return True

    def obtenerArista(self, arista_id):

        if self.dirigido:
            return arista_id in self.aristas
        else:
            a, b = arista_id
            return (a, b) in self.aristas or (b, a) in self.aristas

    def aGraphviz(self, filename, labeln = False, labela = False):

        conector = "--"
        dir = "graph"
        if self.dirigido:
            conector = "->"
            dir = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{dir} {self.id} " + " {\n")
            for nodo in self.nodos:
                if labeln == True:
                    thislabel = self.nodos[nodo].atributos["label"]
                    f.write(f"{nodo}; "+f"[label={thislabel}]\n")
                else:
                    f.write(f"{nodo};\n")
            for arista in self.aristas.values():
                if labela == True:
                    thislabel = arista.atributos["label"]
                    f.write(f"{arista.a} {conector} {arista.b}; "+f"[label={thislabel}]\n")
                else:
                    f.write(f"{arista.a} {conector} {arista.b};\n")
            f.write("}")

    def sorted_dic(self, dict):
        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
        return dict

    def actualization(self, dict):
        if len(dict) != 0:
            dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
            d_i = dict.items()
            first_i = list(d_i)[:1]
            key = first_i[0][0]
            value = first_i[0][1]
            dict.pop(key)
            return dict, key, value
        else:
            return False

    def Dijkstra(self, s):

        T = Grafo(id = f"Dijkstra: {self.id}", dirigido = self.dirigido)
        Nodoi = s
        NInicial = s
        S = {}
        pq = {}
        for nodo in self.nodos:
            #self.nodos[nodo].atributos["label"] = f'"Nodo: {self.nodos[nodo]} Nodo inicial: {self.nodos[0]}"'
            if nodo == Nodoi.id:
                self.nodos[nodo].atributos["peso"] = 0
                self.nodos[nodo].atributos["aristaGanadora"] = None
            else:
                self.nodos[nodo].atributos["peso"] = math.inf
                self.nodos[nodo].atributos["aristaGanadora"] = None
            pq[f"{self.nodos[nodo].id}"] = self.nodos[nodo].atributos["peso"]
            peso = pq[f"{self.nodos[nodo].id}"]
            print(f"Nodo: {self.nodos[nodo].id} Peso: {peso}")
        arr = [9, 14, 15, 24, 18, 30, 5, 20, 44, 11, 16, 6, 6, 2, 19]
        for i, arista in enumerate(self.aristas):
            self.aristas[arista].atributos["peso"] = randrange(1, 50)
            #self.aristas[arista].atributos["peso"] = arr[i]
            peso = self.aristas[arista].atributos["peso"]
            print(f"Arista: {self.aristas[arista].id} Peso: {peso}")

        def vValue(ni, n1, n2):
            if ni == n1:
                return n2
            else:
                return n1

        checker = True

        while checker:
            pq = {k: v for k, v in sorted(pq.items(), key=lambda item: item[1])}
            print(f"PQ: {pq}")
            print(f"S: {S}")

            out = self.actualization(pq)
            if out != False:
                NInicial = int(out[1])
                S[f"{out[1]}"] = out[2]
                pq = out[0]

                print(f"NI: {NInicial}")
                print(f"PQ: {pq}")
                print(f"S: {S}")

                aristas = [arista for arista in self.aristas if NInicial in arista]
                print(aristas)

                for arista in aristas:
                    nodo1 = arista[0]
                    nodo2 = arista[1]
                    # Se obtiene nodo diferente a inicial
                    v = vValue(NInicial, nodo1, nodo2)

                    # valor del último elemento de S
                    d = S[f"{NInicial}"]
                    # valor arista
                    if v == nodo2:
                        Skeys = S.keys()
                        l = self.aristas[arista].atributos["peso"]
                        cont = 0
                        for key in Skeys:
                            if int(key) == int(v):
                                cont = cont + 1
                        if cont > 0:
                            peso = S[f"{v}"]
                        else:
                            peso = pq[f"{v}"]
                        dist = d + l
                        # valor nodo destino
                        print(f"Distancia: {dist} Peso: {peso}")
                        if peso > dist:
                            pq[f"{v}"] = dist
                            self.nodos[v].atributos["aristaGanadora"] = arista
                            self.nodos[v].atributos["peso"] = dist

            else:
                checker = False
        for i, nodo in enumerate(self.nodos):
            self.nodos[nodo].atributos["label"] = f'"Nodo: {self.nodos[nodo]} Nodo inicial: {self.nodos[0]} Peso: {self.nodos[nodo].atributos["peso"]}"'
            print(self.nodos[nodo].atributos)
            if(i!=0):
                var = self.nodos[nodo].atributos["aristaGanadora"]
                if var != None:
                    T.agregarNodo(self.nodos[nodo])
                    T.agregarArista(self.aristas[var])
            else:
                T.agregarNodo(self.nodos[nodo])


        return T

    def KruskalD(self):
        T = Grafo(id = f"KruskalD: {self.id}", dirigido = False)
        aristas = []

        print(f"\n👾Árbol a {len(self.nodos)} nodos:\n")

        def refresh(grupoNod, cont):
            for nodo in self.nodos:
                if self.nodos[nodo].atributos["grupo"] == grupoNod:
                    self.nodos[nodo].atributos["grupo"] = cont
        for nodo in self.nodos:
            self.nodos[nodo].atributos["grupo"] = 0
        for nodo in self.nodos:
            grupo = self.nodos[nodo].atributos["grupo"]
            print(f"Nodo {nodo}: Grupo {grupo}")
        #arr = [4, 6, 16, 24, 23, 5, 8, 10, 21, 11, 14, 9, 7, 18]
        for i, arista in enumerate(self.aristas):
            self.aristas[arista].atributos["peso"] = randrange(1, 50)
            peso = self.aristas[arista].atributos["peso"]
            self.aristas[arista].atributos["label"] = f'"Peso: {peso}"'
            print(f"Arista: {self.aristas[arista].id} Peso: {peso}")
            a = f"{self.aristas[arista].a}"
            b = f"{self.aristas[arista].b}"
            item = [int(a), int(b), int(peso)]
            aristas.append(item)
        aristasFinal = []
        print(f"Aristas: {aristas}")
        aristas = sorted(aristas, key=lambda aristas:aristas[2])
        print(f"Aristas Ordenadas Ascendentemente: {aristas}")

        cont = 1
        for arista in aristas:
            nodo1 = arista[0]
            nodo2 = arista[1]
            grupoNod1 = self.nodos[nodo1].atributos["grupo"]
            grupoNod2 = self.nodos[nodo2].atributos["grupo"]
            if grupoNod1 != grupoNod2:
                aristasFinal.append(arista)
                if grupoNod1 != 0:
                    refresh(grupoNod1, cont)
                else:
                    self.nodos[nodo1].atributos["grupo"] = cont
                if grupoNod2 != 0:
                    refresh(grupoNod2, cont)
                else:
                    self.nodos[nodo2].atributos["grupo"] = cont
                cont = cont + 1
            elif (grupoNod1 == 0) and (grupoNod2 == 0):
                aristasFinal.append(arista)
                self.nodos[nodo1].atributos["grupo"] = cont
                self.nodos[nodo2].atributos["grupo"] = cont
                cont = cont + 1

        for nodo in self.nodos:
            grupo = self.nodos[nodo].atributos["grupo"]
            print(f"Nodo {nodo}: Grupo {grupo}")
        print(f"Aristas Finales (nodo 1, nodo 2, peso arista): {aristasFinal}\n\n")

        for i, nodo in enumerate(self.nodos):
            T.agregarNodo(self.nodos[nodo])

        for arista in self.aristas:
            a = f"{self.aristas[arista].a}"
            b = f"{self.aristas[arista].b}"
            for arista2 in aristasFinal:
                n1 = arista2[0]
                n2 = arista2[1]
                if ((int(a) == n1) and (int(b) == n2)) or ((int(a) == n2) and (int(b) == n1)):
                    T.agregarArista(self.aristas[arista])

        return T

    def KruskalI(self):
        print("Arbol de Kruskal Inverso:")
        T = Grafo(id=f"KruskalI: {self.id}", dirigido=False)
        aristas = []
        descubierto = []
        f = []
        #arr = [4, 6, 16, 24, 23, 5, 8, 10, 21, 11, 14, 9, 7, 18]

        print(f"\n👾Árbol a {len(self.nodos)} nodos:\n")

        def conectEval(a, u=0):
            while True:
                tempAristas = (arista for arista in a if u in arista)
                for arista in tempAristas:
                    v = arista[1] if u == arista[0] else arista[0]
                    if v not in descubierto:
                        f.append((u, v))
                if not f:
                    break
                nod1, nod2 = f.pop()
                if nod2 not in descubierto:
                    descubierto.append(nod2)
                    u = nod2

            if (len(descubierto) != len(self.nodos)):
                #print("Grafo se desconecta")
                #print("------")
                return False
            else:
                #print("Grafo sigue conectado")
                #print("------")
                return True

        for i, arista in enumerate(self.aristas):
            self.aristas[arista].atributos["peso"] = randrange(1, 50)
            peso = self.aristas[arista].atributos["peso"]
            self.aristas[arista].atributos["label"] = f'"Peso: {peso}"'
            print(f"Arista: {self.aristas[arista].id} Peso: {peso}")
            a = f"{self.aristas[arista].a}"
            b = f"{self.aristas[arista].b}"
            item = [int(a), int(b), int(peso)]
            aristas.append(item)

        print(f"Aristas: {aristas}")
        aristas = sorted(aristas, key=lambda aristas:aristas[2], reverse=True)
        print(f"Aristas ordenadas descendentemente: {aristas}")
        temp_aristas = aristas.copy()

        for arista in aristas:
            index = temp_aristas.index(arista)
            del temp_aristas[index]
            descubierto = []
            res = conectEval(temp_aristas)
            if res == False:
                temp_aristas.append(arista)

        print(f"Aristas de árbol resultante (nodo1,nodo2,peso): {temp_aristas}\n\n")

        for i, nodo in enumerate(self.nodos):
            T.agregarNodo(self.nodos[nodo])

        for arista in self.aristas:
            a = f"{self.aristas[arista].a}"
            b = f"{self.aristas[arista].b}"
            for arista2 in temp_aristas:
                n1 = arista2[0]
                n2 = arista2[1]
                if ((int(a) == n1) and (int(b) == n2)) or ((int(a) == n2) and (int(b) == n1)):
                    T.agregarArista(self.aristas[arista])

        return T

    def Prim(self):
        print("Arbol de Prim:")
        T = Grafo(id=f"Prim: {self.id}", dirigido=False)
        aristas = []
        aristasFinal = []
        pila = []
        u = 0
        #arr = [4, 6, 16, 24, 23, 5, 8, 10, 21, 11, 14, 9, 7, 18]
        nodeCont = 0

        print(f"\n👾Árbol a {len(self.nodos)} nodos:\n")

        for nodo in self.nodos:
            self.nodos[nodo].atributos["grupo"] = 0
        for nodo in self.nodos:
            grupo = self.nodos[nodo].atributos["grupo"]
            print(f"Nodo {nodo}: Grupo {grupo}")

        for i, arista in enumerate(self.aristas):
            self.aristas[arista].atributos["peso"] = randrange(1, 50)
            peso = self.aristas[arista].atributos["peso"]
            self.aristas[arista].atributos["label"] = f'"Peso: {peso}"'
            print(f"Arista: {self.aristas[arista].id} Peso: {peso}")
            a = f"{self.aristas[arista].a}"
            b = f"{self.aristas[arista].b}"
            item = [int(a), int(b), int(peso)]
            aristas.append(item)

        print(f"Aristas: {aristas}")

        while nodeCont < (len(self.nodos)-1):
            self.nodos[u].atributos["grupo"] = 1
            nodeCont = nodeCont + 1

            tempAristas = (arista for arista in aristas if u in arista)

            for arista in tempAristas:
                v = arista[1] if u == arista[0] else arista[0]
                p = arista[2]
                gu = self.nodos[u].atributos["grupo"]
                gv = self.nodos[v].atributos["grupo"]

                pila.append([u, v, p])

            print(f"Pila de aristas: {pila}")
            pila = sorted(pila, key=lambda pila: pila[2])
            print(f"Pila ordenada: {pila}")

            while True:
                gu = self.nodos[pila[0][0]].atributos["grupo"]
                gv = self.nodos[pila[0][1]].atributos["grupo"]
                if (gu == 1 and gv == 0):
                    u = pila[0][1]
                    aristasFinal.append(pila[0])
                    del pila[0]
                    break
                else:
                    del pila[0]

            print(f"Aristas Final (nodo1,nodo2,peso): {aristasFinal}")

        for i, nodo in enumerate(self.nodos):
            grupo = self.nodos[nodo].atributos["grupo"]
            print(f"Nodo {nodo}: Grupo {grupo}")
            T.agregarNodo(self.nodos[nodo])

        for arista in self.aristas:
            a = f"{self.aristas[arista].a}"
            b = f"{self.aristas[arista].b}"
            for arista2 in aristasFinal:
                n1 = arista2[0]
                n2 = arista2[1]
                if ((int(a) == n1) and (int(b) == n2)) or ((int(a) == n2) and (int(b) == n1)):
                    T.agregarArista(self.aristas[arista])

        print("\n\n")

        return T


    def BFS(self, s):

        T = Grafo(id = f"BFS: {self.id}", dirigido = self.dirigido)
        descubierto = set()
        T.agregarNodo(s)
        L = []
        Li = [s]

        while True:
            L.append(Li)
            Lj = []
            for node in Li:
                aristas = [arista for arista in self.aristas if node.id in arista]
                print(aristas)
                print("\n\n\n\n")
                for arista in aristas:
                    v = arista[1] if node.id == arista[0] else arista[0]

                    if v in descubierto:
                        continue
                    self.nodos[v].atributos["label"] = f'"Nodo: {self.nodos[v]} Nodo inicial: {self.nodos[0]}"'
                    T.agregarNodo(self.nodos[v])
                    T.agregarArista(self.aristas[arista])
                    descubierto.add(v)
                    Lj.append(self.nodos[v])

            Li = Lj
            if not Li:
                break

        return  T

    def DFS_R(self, u):
        T = Grafo(id=f"DFS_R: {self.id}", dirigido=self.dirigido)
        descubierto = set()
        self.fRecurrente(u, T, descubierto)

        return T

    def fRecurrente(self, u, T, descubierto):

        T.agregarNodo(u)
        descubierto.add(u.id)
        aristas = [arista for arista in self.aristas if u.id in arista]
        print(aristas)
        for arista in aristas:
            v = arista[1]
            if not self.dirigido:
                v = arista[0] if u.id == arista[1] else arista[1]
            if v in descubierto:
                continue
            print(v)
            print(arista)
            print(self.aristas[arista])
            T.agregarArista(self.aristas[arista])
            self.fRecurrente(self.aristas[arista], T, descubierto)

    def DFS_I(self, s):
        T = Grafo(id=f"DFS_I: {self.id}", dirigido=self.dirigido)
        descubierto = {s.id}
        T.agregarNodo(s)
        u = s.id
        f = []
        while True:
            aristas = (arista for arista in self.aristas if u in arista)
            for arista in aristas:
                print(arista)
                v = arista[1] if u == arista[0] else arista[0]
                if v not in descubierto:
                    f.append((u, v))
            print("--------")
            if not f:
                break

            nod1, nod2 = f.pop()

            if nod2 not in descubierto:
                T.agregarNodo(self.nodos[nod2])
                arista = Arista(self.nodos[nod1], self.nodos[nod2])
                T.agregarArista(arista)
                descubierto.add(nod2)

                u = nod2

        return T
