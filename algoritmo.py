import copy
import math

from nodo import *
from tablero import *

# busca en col la primera celda vacía
def busca(tablero, col):  
    if tablero.getCelda(0,col) != 0:
        i=-1
    i=0
    while i<tablero.getAlto() and tablero.getCelda(i,col)==0:          
        i=i+1      
    i=i-1
   
    return i

# llama al algoritmo que decide la jugada
def juega(tablero, posicion):
    ####################################################
    ## sustituir este código por la llamada al algoritmo

    enc=False
    c=0
    while not enc and c<tablero.getAncho():
        f=busca(tablero, c)
        if f!=-1:
            enc=True
        else:
            c=c+1
    if f!=-1:
        posicion[0]=f
        posicion[1]=c
    ####################################################

#Devuelve un arreglo de nodos con las posibles soluciones de dicho nodo
def possibleSolutions(nodo):
    nodosSiguientes = []
    auxTablero = copy.deepcopy(nodo.tablero)
    nodoHijo = None
    for column in range(auxTablero.getAncho()):
        for row in range(auxTablero.getAlto()-1, -1, -1):
            if auxTablero.getCelda(row, column) == 0:
                print('Row ', row)
                print('Column', column)
                #Si el nodo es min el hijo debera ser el contrario
                #Turno de la IA
                if nodo.maxi == True:
                    auxTablero.setCelda(row, column, 2)
                    nodoHijo = Nodo(auxTablero, False)
                #Turno de la persona
                else:
                    auxTablero.setCelda(row, column, 1)
                    nodoHijo = Nodo(auxTablero, True)
                auxNodo = copy.deepcopy(nodoHijo)
                nodosSiguientes.append(auxNodo)
                nodoHijo.tablero.setCelda(row, column, 0)
                print(auxNodo.getTablero())
                break
    nodo.setNodoSiguientes(nodosSiguientes)
    return nodosSiguientes

def minimax(nodo, profundidad, maxi):
    print('PROFUNDIDAD ', profundidad)
    if profundidad == 0 or nodo.tablero.cuatroEnRaya():
        #Debe retornar calcular la funcion de evaluacion
        return nodo
    if maxi:
        maxEval = - math.inf
        for child in possibleSolutions(nodo):
            eval = minimax(child, profundidad - 1, False)
            #maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = math.inf
        for child in possibleSolutions(nodo):
            eval = minimax(child, profundidad - 1, True)
            #minEval = min(minEval, eval)
        return minEval

#def evaluationFunction():
'''
Funcion que retorna un valor dependiendo de la cantidad de piezas
horizontalemnte en el tablero
  '''


'''
def busquedaHorizontal(nodo, profundidad, isMax):
    res = 0
    for column in range(nodo.getTablero().getAlto()):
        for row in range(nodo.getTablero().getAncho()):
            if nodo.maxi() == isMax:
                res += 25

'''














