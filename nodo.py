class Nodo:
    def __init__(self, tablero, mini):
        self.tablero = tablero
        self.nodoSiguientes = []
        self.valor = -1
        self.mini = mini

    def getTablero(self):
        return self.tablero

    def setNodoSiguientes(self, nodos):
        self.nodoSiguientes = nodos

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def getIsMin(self):
        return self.mini

    def setIsMin(self, mini):
        self.mini = mini




