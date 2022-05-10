from arista import Arista

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

    def aGraphviz(self, filename):

        conector = "--"
        dir = "graph"
        if self.dirigido:
            conector = "->"
            dir = "digraph"

        with open(filename, 'w') as f:
            f.write(f"{dir} {self.id} " + " {\n")
            for nodo in self.nodos:
                f.write(f"{nodo};\n")
            for arista in self.aristas.values():
                f.write(f"{arista.a} {conector} {arista.b};\n")
            f.write("}")

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
                for arista in aristas:
                    v = arista[1] if node.id == arista[0] else arista[0]

                    if v in descubierto:
                        continue

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
