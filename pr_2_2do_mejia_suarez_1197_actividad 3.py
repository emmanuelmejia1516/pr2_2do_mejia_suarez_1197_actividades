print("Mejia Suarez Emmanuel Alexander_1197_3w")
def calcular_factorial(n):
    """
    Esta función calcula el factorial de un número entero positivo.
    
    :param n: El número entero positivo cuyo factorial se desea calcular.
    :return: El factorial de 'n'.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

# Ejemplo de uso:
numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")
