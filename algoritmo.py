import copy
import math
import numpy as np

from nodo import *

from tablero import *

TAMVENTANA = 4


# busca en col la primera celda vacía
def busca(tablero, col):
    if tablero.getCelda(0, col) != 0:
        i = -1
    i = 0
    while i < tablero.getAlto() and tablero.getCelda(i, col) == 0:
        i = i + 1
    i = i - 1

    return i


# Devuelve un arreglo de nodos con las posibles soluciones de dicho nodo
def possibleSolutions(nodo):
    nodosSiguientes = []
    auxTablero = copy.deepcopy(nodo.tablero)
    nodoHijo = None
    for column in range(auxTablero.getAncho()):
        for row in range(auxTablero.getAlto() - 1, -1, -1):
            if auxTablero.getCelda(row, column) == 0:
                if nodo.maxi == True:
                    auxTablero.setCelda(row, column, 2)
                    nodoHijo = Nodo(auxTablero, False, row, column)

                else:
                    auxTablero.setCelda(row, column, 1)
                    nodoHijo = Nodo(auxTablero, True, row, column)
                auxNodo = copy.deepcopy(nodoHijo)
                nodosSiguientes.append(auxNodo)
                nodoHijo.tablero.setCelda(row, column, 0)
                break
    nodo.setNodoSiguientes(nodosSiguientes)
    return nodosSiguientes


def minimax(nodo, profundidad, maxi):
    nodo.setNodoSiguientes(possibleSolutions(nodo))
    if profundidad == 0 or nodo.getTablero().cuatroEnRaya():
        print("Profundidad 0 ")
        print("Nodo Valor: ", nodo.getValor())
        return nodo
    if maxi:
        value = - math.inf
        for child in nodo.getNodosSiguientes():
            leaf = minimax(child, profundidad - 1, child.getIsMaxi())
            evalu = evaluation(leaf)
            print("max")
            print("evalu: ", evalu)
            if value < evalu:
                print("Entra un valor: ")
                print(nodo)
                value = evalu
                nodo.setValor(value)
            leaf.setValor(evalu)
            print("value: ", value)

        print("=========================Termino FAMILIA===================================")
        return nodo
    else:
        value = math.inf
        for child in nodo.getNodosSiguientes():
            leaf = minimax(child, profundidad - 1, child.getIsMaxi())
            evalu = evaluation(leaf)
            print("min")
            print("evalu: ", evalu)
            if value > evalu:
                print("Entra un valor: ")
                print(nodo)
                value = evalu
                nodo.setValor(value)
            leaf.setValor(evalu)
            print("value: ", value)

        print("=========================Termino FAMILIA===================================")
        return nodo


def evaluation(nodo):
    puntuacion = 0
    tablero = transformarTablero(nodo)
    if nodo.getIsMaxi():
        opp = 2
        turno = 1
    else:
        opp = 1
        turno = 2

    # puntuacion centro
    colCentro = [int(i) for i in list(tablero[:, nodo.getTablero().getAncho()//2])]
    contCentro = colCentro.count(turno)
    puntuacion += contCentro * 3

    # posicion Horizontal
    for r in range(nodo.getTablero().getAlto()):
        renglon = [int(i) for i in list(tablero[r, :])]
        for c in range(nodo.getTablero().getAncho() - 3):
            ventana = renglon[c:c + TAMVENTANA]
            puntuacion += evaluarVentana(ventana, turno, opp)

    # puntuacion Vertical
    for c in range(nodo.getTablero().getAncho()):
        columna = [int(i) for i in list(tablero[:, c])]
        for r in range(nodo.getTablero().getAlto() - 3):
            ventana = columna[r:r + TAMVENTANA]
            puntuacion += evaluarVentana(ventana, turno, opp)

    # puntuacion diagonales
    for r in range(nodo.getTablero().getAlto() - 3):
        for c in range(nodo.getTablero().getAncho() - 3):
            ventana = [tablero[r + i][c + i] for i in range(TAMVENTANA)]
            puntuacion += evaluarVentana(ventana, turno, opp)

    for r in range(nodo.getTablero().getAlto() - 3):
        for c in range(nodo.getTablero().getAncho() - 3):
            ventana = [tablero[r + 3 - i][c + i] for i in range(TAMVENTANA)]
            puntuacion += evaluarVentana(ventana, turno, opp)

    return puntuacion


def transformarTablero(nodo):
    tablero = np.zeros((nodo.getTablero().getAncho()+1, nodo.getTablero().getAlto()+1))
    for i in range(nodo.getTablero().getAlto()):
        for j in range(nodo.getTablero().getAncho()):
            tablero[i][j] = nodo.getTablero().getCelda(i, j)
    return tablero


def evaluarVentana(window, pieza, opp):
    puntuacion = 0
    if pieza == 2:
        if window.count(pieza) == 4:
            puntuacion += 1000
        elif window.count(pieza) == 3 and window.count(0) == 1:
            puntuacion += 2
        elif window.count(pieza) == 2 and window.count(0) == 2:
            puntuacion += 1
        if window.count(opp) == 3 and window.count(0) == 1:
            puntuacion -= 10
        if window.count(opp) == 2 and window.count(0) == 2:
            puntuacion -= 5
    else:
        if window.count(pieza) == 4:
            puntuacion -= 100
        elif window.count(pieza) == 3 and window.count(0) == 1:
            puntuacion -= 2
        elif window.count(pieza) == 2 and window.count(0) == 2:
            puntuacion -= 1
        if window.count(opp) == 3 and window.count(0) == 1:
            puntuacion += 100
    return puntuacion
