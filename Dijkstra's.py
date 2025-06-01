import sys

# Grafo representado por dos matrices:
# 'conexiones' indica si hay conexion (1) entre nodos
# 'pesos' indica el peso o costo de la conexion entre nodos
conexiones = [[0, 0, 1, 1, 0, 0, 0],
              [0, 0, 1, 0, 0, 1, 0],
              [1, 1, 0, 1, 1, 0, 0],
              [1, 0, 1, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 1, 0],
              [0, 1, 0, 0, 2, 0, 1],
              [0, 0, 0, 1, 0, 1, 0]]

pesos = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]

# Funcion que determina el proximo vertice a visitar
def siguiente_a_visitar():
    global visitado_y_distancia
    indice = -1
    for i in range(numero_vertices):
        no_visitado = visitado_y_distancia[i][0] == 0
        menor_o_primero = (indice < 0 or visitado_y_distancia[i][1] <= visitado_y_distancia[indice][1])
        if no_visitado and menor_o_primero:
            indice = i
    return indice

# Cantidad de vertices (nodos) en el grafo
numero_vertices = len(conexiones[0])

# Lista que guarda para cada nodo:
# [0 si no ha sido visitado, distancia desde el nodo origen]
visitado_y_distancia = [[0, 0]]  # El primer nodo (a) tiene distancia 0
for i in range(numero_vertices - 1):
    visitado_y_distancia.append([0, sys.maxsize])  # Los demas tienen distancia infinita inicialmente

# Algoritmo de Dijkstra
for _ in range(numero_vertices):
    actual = siguiente_a_visitar()
    for vecino in range(numero_vertices):
        hay_conexion = conexiones[actual][vecino] == 1
        no_visitado = visitado_y_distancia[vecino][0] == 0
        if hay_conexion and no_visitado:
            nueva_distancia = visitado_y_distancia[actual][1] + pesos[actual][vecino]
            if nueva_distancia < visitado_y_distancia[vecino][1]:
                visitado_y_distancia[vecino][1] = nueva_distancia
    # Marcar el nodo actual como visitado
    visitado_y_distancia[actual][0] = 1

# Mostrar las distancias minimas desde el nodo origen (a) a todos los demas
for i, distancia in enumerate(visitado_y_distancia):
    letra = chr(ord('a') + i)  # Convertir el indice 0,1,2,... en letras a,b,c,...
    print("Distancia desde el nodo", letra, "al nodo origen: ", distancia[1])
