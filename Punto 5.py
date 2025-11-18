def imprimir_resultado(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print("El resultado de la operación es:", resultado)
        return resultado
    return wrapper
def sumar(a, b):
    return a + b
