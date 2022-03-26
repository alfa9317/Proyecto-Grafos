class Arista(object):

    def __init__(self, a, b, atributos=None):
        self.a = a
        self.b = b
        self.id = (a.id, b.id)
        self.atributos = atributos
