def validar_numero(numero_str):
    """Valida si un número tiene exactamente tres dígitos."""
    return len(numero_str.strip()) == 3 and numero_str.strip().isdigit()

def obtener_numero():
    """Obtiene y valida un número de entrada."""
    while True:
        numero = input("Ingrese un número de tres dígitos: ")
        if validar_numero(numero):
            return int(numero)
        print("Error: Por favor ingrese un número que tenga EXACTAMENTE tres dígitos")

def shellSort(unsorted):
    n = len(unsorted)
    gab = n//2
    
    while gab > 0:
        for i in range(gab, n):
            temp = str(unsorted[i])  # Convertimos a string para comparar longitudes
            j = i
            
            while j >= gab and (len(str(unsorted[j - gab])) > len(temp) or 
                              (len(str(unsorted[j - gab])) == len(temp) and 
                               unsorted[j - gab] > unsorted[i])):
                unsorted[j] = unsorted[j - gab]
                j -= gab
                
            unsorted[j] = unsorted[i]
            
        gab //= 2
    
    return unsorted

# Entrada del usuario
while True:
    try:
        n = int(input("Ingrese cuántos números desea ordenar: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Error: Por favor ingrese un número válido positivo")

# Obtener los números
numeros = []
for i in range(n):
    numero = obtener_numero()
    numeros.append(numero)

# Ordenar y mostrar resultados
numeros_ordenados = shellSort(numeros)
print("\nNúmeros ordenados:")
for numero in numeros_ordenados:
    print(f"{numero:3d}")  # Formateamos para mostrar siempre tres dígitos30