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
        pos_list = []
        max_val = self.getNodoRaiz().getValor()
        for pos, child_fg in enumerate(self.getNodoRaiz().getNodosSiguientes()):
            print("NODO HIJO: ", pos)
            print(child_fg.getValor())
            print(child_fg.getTablero())
            if child_fg.getValor() == max_val:
                pos_list.append(pos)
        if len(pos_list) == 1:
            return pos_list[0]
        random_pos = random.randint(0, len(pos_list)-1)
        return pos_list[random_pos]






