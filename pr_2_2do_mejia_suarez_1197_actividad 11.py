print("Mejia Suarez Emmanuel Alexander_1197_3w")
import math

def distancia_puntos(x1, y1, x2, y2):
    # Calcula la distancia entre dos puntos en un plano cartesiano.
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Ejemplo
print(distancia_puntos(1, 2, 4, 6))  # 5.0
print(distancia_puntos(0, 0, 3, 4))  # 5.0
