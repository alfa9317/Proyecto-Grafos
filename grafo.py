from arista import Arista
from random import randrange
import math

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

    def aGraphviz(self, filename, label = False):

        conector = "--"
        dir = "graph"
        if self.dirigido:
            conector = "->"
            dir = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{dir} {self.id} " + " {\n")
            for nodo in self.nodos:
                if label == True:
                    thislabel = self.nodos[nodo].atributos["label"]
                    f.write(f"{nodo}; "+f"[label={thislabel}]\n")
                else:
                    f.write(f"{nodo};\n")
            for arista in self.aristas.values():
                f.write(f"{arista.a} {conector} {arista.b};\n")
            f.write("}")

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
                v = arista[1] if u == arista[0] else arista[0]
                if v not in descubierto:
                    f.append((u, v))
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
