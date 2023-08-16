def suma(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido."

def resta(a, b):
    try:
        result = a - b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido."

def producto(a, b):
    try:
        result = a * b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido."

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        result = a / b
        return result
    except (ZeroDivisionError, TypeError):
        return "Error: No es posible dividir entre cero."
