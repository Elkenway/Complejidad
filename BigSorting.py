def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

print("Ingrese los numeros a ordenar separados por espacios: ")
unsorted = input().strip().split()

# Ordenar la lista
sorted_list = bigSorting(unsorted)

# Imprimir la lista ordenada
print("Numeros ordenados: ")
print(" ".join(sorted_list))
