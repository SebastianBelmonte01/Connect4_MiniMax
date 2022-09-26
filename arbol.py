class Arbol:
    def __init__(self):
        self.nodoRaiz = None

    def getNodoRaiz(self):
        return self.nodoRaiz

    def setNodoRaiz(self, root):
        self.nodoRaiz = root

    def isEmpty(self):
        if self.nodoRaiz == None:
            return True
        else:
            return False



