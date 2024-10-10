print("Mejia Suarez Emmanuel Alexander_1197_3w")
def longitud_ultima_palabra(cadena):
    # Devuelve la longitud de la última palabra en una cadena. Ignora espacios adicionales.
    palabras = cadena.split()
    if palabras:
        return len(palabras[-1])
    else:
        return 0  # Si no hay palabras, la longitud es 0.

# Ejemplo
print(longitud_ultima_palabra("Hola mundo "))          # 5
print(longitud_ultima_palabra(" Python es increíble "))  # 9
