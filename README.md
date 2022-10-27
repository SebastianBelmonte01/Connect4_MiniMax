En la presente documentación se muestra el funcionamiento del algoritmo Minimax y Minimax con podas alfa beta. Dentro del programa en cuestión, se definió a Max como la persona ya que es la que inicia con el juego y por ende, Min será la IA. 
Además se implementaron dos clases más para poder manipular y almacenar los datos en el árbol. Una de estas clases fue denominada; nodo, la cual posee diferentes atributos como el tablero, un valor, entre otros. La creación de dicha clase nos permite generar un árbol la cual posee un nodo raíz.

Minimax genera un árbol con una cierta profundidad; sin embargo el algoritmo Minimax con podas corta algunas ramas por visitar del árbol. Esto genera que sea posible aumentar la profundidad del árbol haciendo que sea más difícil ganar a la IA.

Se realizaron dos funciones de evaluación donde la primera presentaba problemas a la hora de asignar un valor al nodo con el tablero en cuestión. Sin embargo, el segundo al poseer más condiciones y puntajes generan más exactitud a la hora de realizar una jugada. Gracias a ello la IA puede atacar y defenderse si es que el oponente posee una mejor posición.
