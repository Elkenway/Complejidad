from itertools import permutations, combinations

def factorial(n):
    #Se calcula el factorial de un número 
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def permutaciones_recursivas(lista):
    #se generan permutaciones
    if len(lista) == 1:
        return [lista]
    
    permutaciones = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]  #Lista sin el elemento actual
        for p in permutaciones_recursivas(resto):
            permutaciones.append([lista[i]] + p)
    
    return permutaciones

def combinaciones_recursivas(lista, k, start=0, path=[]):
    #Se generan combinaciones recursivamente
    if len(path) == k:
        print(tuple(path))  #Se imprime la combinacion encontrada
        return
    
    for i in range(start, len(lista)):
        combinaciones_recursivas(lista, k, i + 1, path + [lista[i]])

# Número del documento (cambiarlo según el caso)
documento = int(input("Ingrese el número de documento: "))

# Conjunto de elementos
elementos = ['A', 'B', 'C', 'D']  # Puedes modificarlo según necesidad

if documento % 2 == 0:
    print("\nEl documento es PAR -> Calculando permutaciones:")
    
    # Método con ciclos
    print("Permutaciones con itertools:")
    for p in permutations(elementos):
        print(p)

    # Método recursivo
    print("\nPermutaciones con recursividad:")
    for p in permutaciones_recursivas(elementos):
        print(tuple(p))

else:
    print("\nEl documento es IMPAR -> Calculando combinaciones de 2 elementos:")

    # Método con ciclos
    print("Combinaciones con itertools:")
    for c in combinations(elementos, 2):
        print(c)

    # Método recursivo
    print("\nCombinaciones con recursividad:")
    combinaciones_recursivas(elementos, 2)
