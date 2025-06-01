#Sudoku

tablero = [
    [1,0,4,0,2,0,5,0,3],
    [0,8,0,3,0,1,0,0,0],
    [2,9,3,0,0,5,0,0,1],
    [0,0,2,0,6,0,0,0,5],
    [0,0,0,4,0,8,0,0,0],
    [9,0,0,0,5,0,7,0,0],
    [5,0,0,6,0,0,8,3,2],
    [0,0,0,5,0,2,0,4,0],
    [4,0,8,0,3,0,9,0,6]
]

def es_tablero_valido(tablero):
    # Verifica si el tablero cumple con las reglas del Sudoku
    for fila in range(9):
        nums = [n for n in tablero[fila] if n != 0]
        if len(set(nums)) != len(nums):
            return False
    
        # Comprueba que no haya números repetidos en las columnas
    for columna in range(9):
        nums = [tablero[fila][columna] for fila in range(9) if tablero[fila][columna] != 0]
        if len(set(nums)) != len(nums):
            return False
        #Comprueba que no haya números repetidos en las casillas de 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = [tablero[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if tablero[x][y] != 0]
            if len(set(nums)) != len(nums):
                return False
    
    return True

def generar_combinaciones(vacios, index, tablero):
    # Genera combinaciones de números del 1 al 9 en las celdas vacías de manera recursiva
    if index == len(vacios):
        return es_tablero_valido(tablero)
       
     # Obtiene la fila y la columna de la celda vacía actual
    fila, columna = vacios[index]
    
    # Coloca los valores posibles para la celda vacía actual de 1 a 9
    for num in range(1, 10):
        tablero[fila][columna] = num
        #Se valida si la combinación es válida
        if es_tablero_valido(tablero) and generar_combinaciones(vacios, index + 1, tablero):
            return True
        #Si no es válida, se resetea la celda a 0 y se sigue con la siguiente
        tablero[fila][columna] = 0
    
    return False

def resolver_sudoku_fuerza_bruta_extrema(tablero):
    # Encuentra todas las celdas vacías en el tablero
    vacios = [(i, j) for i in range(9) for j in range(9) if tablero[i][j] == 0]
    #Se realiza el intento de resolver las casillas vacías
    return generar_combinaciones(vacios, 0, tablero)

def imprimir_tablero(tablero):
    # Imprime el tablero del Sudoku de manera organizada
    for i in range(len(tablero)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(tablero[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")
                
print("Sudoku Original:")
imprimir_tablero(tablero)

if resolver_sudoku_fuerza_bruta_extrema(tablero):
    print("\nSudoku solucionado:")
    imprimir_tablero(tablero)
else:
    print("No existe solución")
