def es_palindromo(x: int) -> bool:
    """Verifica si un número entero es un palíndromo."""
    if x < 0:
        return False  # Un número negativo nunca es palíndromo
    
    num_str = str(x)
    return num_str == num_str[::-1]

def main():
    """Función principal para interactuar con el usuario."""
    while True:
        try:
            # Se solicita el numero al usuario
            x = input("\nIngrese un número para verificar si es palíndromo (o 'q' para salir): ")
            
            # Verificar si el usuario quiere cancelar
            if x.lower() == 'q':
                print("¡Hasta luego!")
                break
            
            # se convierte lo ingresado a entero
            x = int(x)
            
            # Se verifica que el rango este dentro de los permitidos
            if not (-2**31 <= x <= 2**31 - 1):
                print("Error: El número debe estar entre -2,147,483,648 y 2,147,483,647.")
                continue
            
            # Se verifica si es paliandro
            if es_palindromo(x):
                print(f"El número {x} es un palíndromo.")
            else:
                print(f"El número {x} no es un palíndromo.")
                
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    print("Programa para verificar números palíndromos")
    print("Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda.")
    print("Ejemplos: 121, 12321. Nota: los números negativos no son palíndromos.")
    main()
