import sys, pygame
from tablero import *
from algoritmo import *
from pygame.locals import *
from arbol import *
import time

MARGEN = 20
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
NARANJA = (254, 115, 28)
TAM = 60

def main():
    pygame.init()

    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode([700, 620])
    pygame.display.set_caption("Belmonte Sebastian - Practica 1")

    # Intancia de Arbol
    arbol = Arbol(1)
    # Nodo Actual
    nodoRaiz = None

    # Nodo Anterior
    nuevo = None
    next_move = 0

    game_over = False
    tablero = Tablero(None)
    col = -1
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # obtener posición y calcular coordenadas matriciales
                # juega persona, comprobar casilla y actualizar tablero
                pos = pygame.mouse.get_pos()
                colDestino = (pos[0] - (2 * MARGEN)) // (TAM + MARGEN)
                # comprobar que es una posición válida
                fila = busca(tablero, colDestino)
                if fila != -1:
                    nodosVisitados = []
                    # Si el arbol esta vacio se le agreaga el nodo raiz
                    tablero.setCelda(fila, colDestino, 1)
                    nodoRaiz = Nodo(tablero, True, fila, col)
                    arbol.setNodoRaiz(nodoRaiz)
                    # arbol.getNodoRaiz().setNodoSiguientes(possibleSolutions(nodoRaiz))

                    inicio = time.time()
                    minimax(nodoRaiz, arbol.getProfundiad(), nodoRaiz.getIsMaxi(), nodosVisitados)
                    next_move = arbol.siguienteMovimiento()
                    print("Nodo RAIZ VALOR: ", nodoRaiz.getValor())
                    nodoRaiz = nodoRaiz.getNodoSiguientes(next_move)
                    #print(nodoRaiz.getTablero())
                    fin = time.time()

                    print("Tiempo transcurrido: ")
                    print(fin-inicio)
                    print("Nodos visitados")
                    print(len(nodosVisitados)+1)
                    print("=========================Termino FAMILIA===================================")

                if tablero.cuatroEnRaya() == 1:
                    game_over = True
                    print("gana persona")
                else:  # si la persona no ha ganado, juega la máquina
                    #posicion = [-1, -1]
                    #juega(tablero, posicion)
                    #Se debe obtener el nodo siguiente y las coordenadas del mismo
                    #print('NUEVO', nuevo.getIndiceSiguienteMovimiento())
                    #tablero.setCelda(nuevo.getNodoSiguientes(nuevo.getIndiceSiguienteMovimiento()).getX(), nuevo.getNodoSiguiente(nuevo.getIndiceSiguienteMovimiento()).getY(), 2)
                    tablero.setCelda(nodoRaiz.getX(), nodoRaiz.getY(), 2)
                    if tablero.cuatroEnRaya() == 2:
                        game_over = True
                        print("gana máquina")
        # código de dibujo
        # limpiar pantalla
        screen.fill(NEGRO)
        pygame.draw.rect(screen, AZUL, [MARGEN, MARGEN, 660, 580], 0)
        for fil in range(tablero.getAlto()):
            for col in range(tablero.getAncho()):
                if tablero.getCelda(fil, col) == 0:
                    pygame.draw.ellipse(screen, BLANCO,
                                        [(TAM + MARGEN) * col + 2 * MARGEN, (TAM + MARGEN) * fil + 2 * MARGEN, TAM,
                                         TAM], 0)
                elif tablero.getCelda(fil, col) == 1:
                    pygame.draw.ellipse(screen, ROJO,
                                        [(TAM + MARGEN) * col + 2 * MARGEN, (TAM + MARGEN) * fil + 2 * MARGEN, TAM,
                                         TAM], 0)
                else:
                    pygame.draw.ellipse(screen, AMARILLO,
                                         [(TAM + MARGEN) * col + 2 * MARGEN, (TAM + MARGEN) * fil + 2 * MARGEN, TAM,
                                         TAM], 0)
        for col in range(tablero.getAncho()):
            pygame.draw.rect(screen, BLANCO, [(TAM + MARGEN) * col + 2 * MARGEN, 10, TAM, 10], 0)

        # actualizar pantalla
        pygame.display.flip()
        reloj.tick(40)
        if game_over == True:  # retardo cuando gana
            pygame.time.delay(1500)

    pygame.quit()


if __name__ == "__main__":
    main()

