def super_digit(n, k):
    # Sumar los digitos de n y multiplicar por k
    initial_sum = sum(int(digit) for digit in str(n)) * k

    # Funcion recursiva para calcular el superdigito
    def recursive_super_digit(x):
        if x < 10:  # Si ya es un solo digito, devolverlo
            return x
        return recursive_super_digit(sum(int(d) for d in str(x)))

    return recursive_super_digit(initial_sum)

# Leer entrada en formato esperado (n y k separados por espacio)
n, k = input().split()
k = int(k)

# Imprimir el resultado
print(super_digit(n, k))
