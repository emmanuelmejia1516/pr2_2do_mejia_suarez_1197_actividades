print("Mejia Suarez Emmanuel Alexander_1197_3w")
def mayor_de_tres(num1, num2, num3):
    """
    Esta función toma tres números como argumentos
    y devuelve el mayor de ellos.
    
    Parámetros:
    num1 (int, float): Primer número.
    num2 (int, float): Segundo número.
    num3 (int, float): Tercer número.
    
    Retorna:
    int, float: El número mayor entre los tres.
    """
    # Inicializamos una variable para almacenar el mayor número
    mayor = num1
    
    # Comparamos num2 con el mayor actual
    if num2 > mayor:
        mayor = num2
    
    # Comparamos num3 con el mayor actual
    if num3 > mayor:
        mayor = num3
    
    return mayor

# Ejemplo de uso de la función
if __name__ == "__main__":
    # Solicitamos al usuario que ingrese tres números
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    n3 = float(input("Ingresa el tercer número: "))
    
    # Llamamos a la función y mostramos el resultado
    resultado = mayor_de_tres(n1, n2, n3)
    print(f"El mayor de los tres números es: {resultado}")
