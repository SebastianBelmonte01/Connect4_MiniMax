import random
import numpy


class Arbol:
    def __init__(self, profundidad):
        self.nodoRaiz = None
        self.profundiad = profundidad

    def getNodoRaiz(self):
        return self.nodoRaiz

    def setNodoRaiz(self, root):
        self.nodoRaiz = root

    def isEmpty(self):
        if self.nodoRaiz == None:
            return True
        else:
            return False
    def getProfundiad(self):
        return self.profundiad

    '''

    def siguienteMovimiento(self):
        nodos_hijos = self.getNodoRaiz().getNodosSiguientes()
        pos_list = []
        rand_pos = 0
        for i, nodo in enumerate(nodos_hijos):
            print(nodo.getValor())
            print(nodo.getTablero())

        for pos, child_fg in enumerate(self.getNodoRaiz().getNodosSiguientes()):
            if child_fg.getValor() == self.nodoRaiz.getValor():
                print("YAVLA")
                print(child_fg.getTablero())
                pos_list.append(pos)
        if len(pos_list) == 0:
            print("El TAMAÑO es : ", len(pos_list))
            return 0
        if len(pos_list) == 1:
            return pos_list[rand_pos]
        print("RANDOM")
        rand_pos = random.randint(0, len(pos_list)-1)
        return pos_list[rand_pos]
'''

    def siguienteMovimiento(self):
        nodos_hijos = self.getNodoRaiz().getNodosSiguientes()
        pos_list = []
        rand_pos = 0
        aux = numpy.zeros(len(nodos_hijos))
        for i, nodo in enumerate(nodos_hijos):
            aux[i] = nodo.getValor()
            print(nodo.getValor())
            print(nodo.getTablero())

        max_val = numpy.min(aux)
        print("EL VALOR ES: ", max_val)
        #Primero verificar si es que existe más de una solucion con el mismo peso
        #Guardar en un arrya todas las soluciones con el mismo peso [pos, pos1, ... , posR]
        #Seleccionar Randomicamente una de esas posiciones y retornarala
        for pos, child_fg in enumerate(self.getNodoRaiz().getNodosSiguientes()):
            if child_fg.getValor() == max_val:
                pos_list.append(pos)

        if len(pos_list) == 1:
            return pos_list[rand_pos]
        print("RANDOM")
        rand_pos = random.randint(0, len(pos_list)-1)
        return pos_list[rand_pos]






