def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

# Leer la cantidad de números
n = int(input())

# Leer los números en formato de cadena
unsorted = [input().strip() for _ in range(n)]

# Ordenar la lista
sorted_list = bigSorting(unsorted)

# Imprimir los números ordenados
for num in sorted_list:
    print(num)

