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

    def siguienteMovimiento(self):

        '''
                nodos_hijos = self.getNodoRaiz().getNodosSiguientes()
        pos_list = []
        rand_pos = 0
        sumaCeros = 0
        aux = numpy.zeros(len(nodos_hijos))
        for i, nodo in enumerate(nodos_hijos):
            aux[i] = nodo.getValor()
            if aux[i] == 0:
                sumaCeros += 1
            print(nodo.getValor())
            print(nodo.getTablero())
        if sumaCeros >= 1:
            max_val = 0
        else:

        :return:
        '''
        pos_list = []
        max_val = self.getNodoRaiz().getValor()
        print("EL VALOR ES: ", max_val)
        #Primero verificar si es que existe más de una solucion con el mismo peso
        #Guardar en un arrya todas las so luciones con el mismo peso [pos, pos1, ... , posR]
        #Seleccionar Randomicamente una de esas posiciones y retornarala
        for pos, child_fg in enumerate(self.getNodoRaiz().getNodosSiguientes()):
            print("Valor: ", child_fg.getValor())
            print(child_fg.getTablero())
            if child_fg.getValor() == max_val:
                pos_list.append(pos)
        if len(pos_list) == 1:
            return pos_list[0]
        print("RANDOM")
        random_pos = random.randint(0, len(pos_list)-1)
        print(random_pos)
        return pos_list[random_pos]






