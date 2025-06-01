lista = [3, 5, 7, 10, 14, 18]
#La búsqueda binaria divide el espacio de búsqueda a la mitad en cada iteración,
    #por lo que es más eficiente que la búsqueda lineal, pero requiere que la lista
    #esté previamente ordenada.

def busqueda_binaria(lista, objetivo): #    Realiza una búsqueda binaria en una lista ordenada.

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1 # Buscar en la mitad derecha
        else:
            fin = medio - 1 # Buscar en la mitad izquierda
    return -1 #Si se retorna un -1 es porque el elemento no fue encontrado

print("Búsqueda binaria:")
print(busqueda_binaria(lista, 18))  