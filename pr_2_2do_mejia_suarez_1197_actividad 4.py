print("Mejia Suarez Emmanuel Alexander_1197_3w")
def calcular_total_factura(cantidad_sin_iva, iva=21):
    """
    Esta función calcula el total de una factura después de aplicar el IVA.
    
    :param cantidad_sin_iva: El monto total de la factura sin IVA.
    :param iva: El porcentaje de IVA a aplicar. Por defecto es 21%.
    :return: El total de la factura con IVA incluido.
    """
    iva_aplicado = (iva / 100) * cantidad_sin_iva
    total_factura = cantidad_sin_iva + iva_aplicado
    return total_factura

# Ejemplo de uso:
factura_sin_iva = 100
print(f"El total de la factura es {calcular_total_factura(factura_sin_iva)}")
