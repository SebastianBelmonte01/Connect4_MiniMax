class Nodo:
    def __init__(self, tablero, maxi):
        self.tablero = tablero
        self.nodoSiguientes = []
        self.valor = -1
        self.maxi = maxi

    def getTablero(self):
        return self.tablero

    def setNodoSiguientes(self, nodos):
        self.nodoSiguientes = nodos

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def getIsMaxi(self):
        return self.maxi

    def setIsMaxi(self, maxi):
        self.maxi = maxi




