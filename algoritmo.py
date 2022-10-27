import copy
import math
import numpy as np

from nodo import *

from tablero import *

NODOS = 0


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


def minimax(nodo, profundidad, maxi, nodosVisitados):
    nodo.setNodoSiguientes(possibleSolutions(nodo))
    if profundidad == 0 or nodo.getTablero().cuatroEnRaya():
        return nodo
    if maxi:
        value = - math.inf
        for child in nodo.getNodosSiguientes():
            nodosVisitados.append(child)
            leaf = minimax(child, profundidad - 1, child.getIsMaxi(), nodosVisitados)
            evalu = evaluation(leaf)
            if value < evalu:
                value = evalu
                nodo.setValor(value)
            leaf.setValor(evalu)
        return nodo
    else:
        value = math.inf
        for child in nodo.getNodosSiguientes():
            nodosVisitados.append(child)
            leaf = minimax(child, profundidad - 1, child.getIsMaxi(), nodosVisitados)
            evalu = evaluation(leaf)
            if value > evalu:
                value = evalu
                nodo.setValor(value)
            leaf.setValor(evalu)
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

    for r in range(nodo.getTablero().getAlto()):
        fila = [int(i) for i in list(tablero[r, :])]
        for c in range(nodo.getTablero().getAncho() - 3):
            filas = fila[c:c + 4]
            puntuacion += calcularValor(filas, turno, opp)

    # puntuacion Vertical
    for c in range(nodo.getTablero().getAncho()):
        columna = [int(i) for i in list(tablero[:, c])]
        for r in range(nodo.getTablero().getAlto() - 3):
            columnas = columna[r:r + 4]
            puntuacion += calcularValor(columnas, turno, opp)

    # puntuacion diagonales
    for r in range(nodo.getTablero().getAlto() - 3):
        for c in range(nodo.getTablero().getAncho() - 3):
            diagonales = [tablero[r + i][c + i] for i in range(4)]
            puntuacion += calcularValor(diagonales, turno, opp)

    for r in range(nodo.getTablero().getAlto() - 3):
        for c in range(nodo.getTablero().getAncho() - 3):
            diagnoales_der = [tablero[r + 3 - i][c + i] for i in range(4)]
            puntuacion += calcularValor(diagnoales_der, turno, opp)

    centro = [int(i) for i in list(tablero[:, nodo.getTablero().getAncho()//2])]
    cantidadPiezasCentro = centro.count(turno)
    puntuacion += cantidadPiezasCentro * 3

    return puntuacion


def transformarTablero(nodo):
    tablero = np.zeros((nodo.getTablero().getAncho()+1, nodo.getTablero().getAlto()+1))
    for i in range(nodo.getTablero().getAlto()):
        for j in range(nodo.getTablero().getAncho()):
            tablero[i][j] = nodo.getTablero().getCelda(i, j)
    return tablero


def calcularValor(window, pieza, opp):
    puntuacion = 0
    if pieza == 1:
        if window.count(pieza) == 4:
            puntuacion -= 100
        elif window.count(pieza) == 3 and window.count(0) == 1:
            puntuacion -= 2
        elif window.count(pieza) == 2 and window.count(0) == 2:
            puntuacion -= 1
        if window.count(opp) == 3 and window.count(0) == 1:
            puntuacion += 100
    else:
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
    return puntuacion

'''

def calcularValor(window, pieza, opp):
    puntuacion = 0
    if window.count(pieza) == 4:
        puntuacion += 100
    elif window.count(pieza) == 3 and window.count(0) == 1:
        puntuacion += 5
    elif window.count(pieza) == 2 and window.count(0) == 2:
        puntuacion += 2
    if window.count(opp) == 3 and window.count(0) == 1:
        puntuacion -= 4
    return puntuacion

'''
