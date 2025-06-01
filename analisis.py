import random

print("Ingrese cuantos numeros aleatorios desea obtener:")
n = int(input())

aleatorios = [random.randint(0, 1000) for _ in range(n)]
print("Numeros generados:", aleatorios)

def encontrar_min(lista):
    if not lista:
        return None  
    
    minimo = lista[0]  
    
    for numero in lista:  
        if numero < minimo:  
            minimo = numero  
    return minimo  

minimo = encontrar_min(aleatorios)
print("El numero mínimo en la lista es:", minimo)