class Nodo:
    def __init__(self, tablero, maxi, x, y):
        self.tablero = tablero
        self.nodoSiguientes = []
        self.valor = 0
        #Maxi es la IA
        self.maxi = maxi
        self.x = x
        self.y = y


    def getTablero(self):
        return self.tablero

    def setNodoSiguientes(self, nodos):
        self.nodoSiguientes = nodos
    def getNodoSiguientes(self, pos):
        return self.nodoSiguientes[pos]


    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def getIsMaxi(self):
        return self.maxi

    def setIsMaxi(self, maxi):
        self.maxi = maxi
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    def getNodosSiguientes(self):
        return self.nodoSiguientes

    def setIndiceSiguienteMovimeinto(self, indice):
        self.indiceSiguienteMovimiento = indice

    def getIndiceSiguienteMovimiento(self):
        return self.indiceSiguienteMovimiento


