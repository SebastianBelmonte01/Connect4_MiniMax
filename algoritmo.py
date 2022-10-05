import copy
import math
import random
from filecmp import cmp

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
                #print('Row ', row)
                #print('Column', column)
                #Si el nodo es min el hijo debera ser el contrario
                #Turno de la IA
                #TODO VALIDAR LAS REGLAS DEL JUEGO; SI ES PERMITIDO
                #SE ASIGNA EL VALOR
                if nodo.maxi == True:
                    auxTablero.setCelda(row, column, 2)
                    nodoHijo = Nodo(auxTablero, False, row, column)
                #Turno de la persona
                else:
                    auxTablero.setCelda(row, column, 1)
                    nodoHijo = Nodo(auxTablero, True, row, column)
                auxNodo = copy.deepcopy(nodoHijo)
                nodosSiguientes.append(auxNodo)
                nodoHijo.tablero.setCelda(row, column, 0)
                #print(auxNodo.getTablero())
                break
    nodo.setNodoSiguientes(nodosSiguientes)
    return nodosSiguientes

def minimax(nodo, profundidad, maxi):
    #print("Profundiad ", profundidad)
    #print('Nodo Padre')
    #print('Is max? ', maxi)
    #print(nodo.getX(), " - ", nodo.getY())
    print(nodo.getTablero())
    if profundidad == 0 or nodo.tablero.cuatroEnRaya():
        #Debe retornar calcular la funcion de evaluacion
        nodo.setValor(random.randint(1, 9))
        return nodo

    if maxi:
        maxEval = - math.inf
        nodoHijo = None
        for child in possibleSolutions(nodo):

            #print('Hijo de Max, ', child.getTablero())
            eval = minimax(child, profundidad - 1, False)
            if nodoHijo == None:
                nodoHijo = eval
            else:
                if cmp(nodoHijo.getValor(), eval.getValor()) < 0:
                    nodoHijo = eval
            #print('Max')
            #print(child.getTablero())
        nodo.setValor(nodoHijo.getValor())
        print('Evaluation: ', nodo.getValor())

        return nodo

    else:
        minEval = math.inf
        nodoHijo = None

        for child in possibleSolutions(nodo):
            #print('Hijo de Min, ', child.getTablero())
            eval = minimax(child, profundidad - 1, True)
            if nodoHijo == None:
                nodoHijo = eval
            print('Valor nodo hijo ', nodoHijo.getValor())
            print('Valor nodo eval ', eval.getValor())

            if cmp(nodoHijo.getValor(), eval.getValor()) > 0:
                 nodoHijo = eval
                #print('Min')
            #print(child.getTablero())
        nodo.setValor(nodoHijo.getValor())
        print('Evaluation: ', nodo.getValor())

        return nodo

'''

def evaluationFunction(nodo):
    return busquedaHorizontal(nodo)


Funcion que retorna un valor dependiendo de la cantidad de piezas
horizontalemnte en el tablero

Si es que es max será un número positivo, si es que no es max 

será un número negativo


Primero dividir todas las posibles formas de ganar en un vector
    - Horizontal
    - Vertical
    - Diagonal izq
    - Diagonal der

Segundo utilizar una funcion de evaluacion

'''

def evaluation(nodo):
    return filaHorizontal(nodo)


def filaHorizontal(nodo):
    total = 0
    for i in range(nodo.getTablero().getAlto()):
        fila = []
        for j in range(nodo.getTablero().getAncho()):
            fila.append(nodo.getTablero().getCelda(i, j))
        #total += random.randint(1, 9)
        total += evaluate_array(fila, nodo)
    #print('El total es igual a ', total)
    return total

def evaluate_array(filas, nodo):
    score = 0
    for arr in permutations(filas):
        #print ('Arreglo: ', arr)
        #Se juega como la IA
        if nodo.getIsMaxi():
            opp = 1
            piece = 2
        #Se juega como persona
        else:
            opp = 2
            piece = 1

        if arr.count(piece) == 4:
            score += 100
        elif arr.count(piece) == 3 and arr.count(0) == 1:
            score += 5
        elif arr.count(piece) == 2 and arr.count(0) == 2:
            score += 2
        if arr.count(opp) == 3 and arr.count(0) == 1:
            score -= 4
    return random.randint(1, 9)

def permutations(array):
    return (array[j:j + 4] for j in range(0, len(array) - (4 - 1)))

