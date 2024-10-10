print("Mejia Suarez Emmanuel Alexander_1197_3w")
def validar_email(email):
    # Verifica si una dirección de email es válida revisando si contiene '@'.
    if '@' in email:
        return "La dirección de email es válida."
    else:
        return "La dirección de email no es válida."

# Ejemplo
print(validar_email("ejemplo@correo.com"))  # La dirección de email es válida.
print(validar_email("ejemplocorreo.com"))    # La dirección de email no es válida.
