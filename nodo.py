class Nodo(object):

    def __init__(self, id, atributos=None):
        self.id = id

        if atributos is None:
            self.atributos = {}

        else:
            self.atributos = atributos

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return f'{self.id}'