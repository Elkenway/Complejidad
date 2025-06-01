lista = [14, 5, 72, 1, 12, 8]

#Recorre todos los elementos uno por uno hasta encontrar el objetivo.
def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  # devuelve el índice donde se encontró
    return -1  # si no se encontró

print("Búsqueda lineal:")
print(busqueda_lineal(lista, 72)) #El numero resultante es cuantos espacios se tuvo que mover
                                   # para hallar el numero bucado