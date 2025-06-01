
def burbuja_ord(arreglo): #Se define la funcion del ordenamiento
    n = len(arreglo)
    
    # Ciclo externo: controla cuántas pasadas se harán
    for i in range(n - 1):
        intercambio = False #Se verifican los intercambios
 
    
 # Ciclo interno: compara elementos adyacentes 
        for j in range(n - 1 - i):
            if arreglo[j] > arreglo[j+1] :
                # Intercambia los elementos si están en el orden incorrecto
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
                intercambio = True # aqui se realizó al menos un intercambio
 
    #Si ya noy hy mas intercambios se rompe el ciclo
        if not intercambio == False:
            break

elementos = ["Complejidad", "Estadistica", "Calculo", "DOO", "Bases de datos", "Algoritmos", "Programacion"] #Lista a ordenar
burbuja_ord(elementos)

#Se imprimen los elementos de la lista "elementos" de manera alfabetica
print(elementos) 
    