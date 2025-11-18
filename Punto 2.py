def area_rectangulo(anchura, altura):
    return anchura * altura

anchura = float(input("Ingrese la anchura del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

resultado = area_rectangulo(anchura, altura)
print("El área del rectángulo es:", resultado)