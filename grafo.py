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
