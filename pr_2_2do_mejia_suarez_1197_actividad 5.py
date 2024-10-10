print("Mejia Suarez Emmanuel Alexander_1197_3w")
import math

def calcular_area_circulo(radio):
    """
    Esta función calcula el área de un círculo dado su radio.
    
    :param radio: El radio del círculo.
    :return: El área del círculo.
    """
    return math.pi * radio ** 2

def calcular_volumen_esfera(radio):
    """
    Esta función calcula el volumen de una esfera dado su radio.
    
    :param radio: El radio de la esfera.
    :return: El volumen de la esfera.
    """
    return (4/3) * math.pi * radio ** 3

# Ejemplo de uso:
radio_circulo = 3
radio_esfera = 3

print(f"El área del círculo es {calcular_area_circulo(radio_circulo)}")
print(f"El volumen de la esfera es {calcular_volumen_esfera(radio_esfera)}")
print()
def calcular_volumen_cilindro(radio, altura):
    """
    Esta función calcula el volumen de un cilindro usando el área de su base circular.
    
    :param radio: El radio de la base del cilindro.
    :param altura: La altura del cilindro.
    :return: El volumen del cilindro.
    """
    area_base = calcular_area_circulo(radio)
    return area_base * altura

# Ejemplo de uso:
radio_cilindro = 3
altura_cilindro = 5

print(f"El volumen del cilindro es {calcular_volumen_cilindro(radio_cilindro, altura_cilindro)}")