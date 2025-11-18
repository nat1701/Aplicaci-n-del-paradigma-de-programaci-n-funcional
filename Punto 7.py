def generar_identificador(nombre_completo, dni):
    partes = nombre_completo.split()

    # Primer nombre
    primer_nombre = partes[0]

    # Apellido (última palabra ingresada)
    apellido = partes[-1]

    # Cantidad de letras del apellido
    letras_apellido = len(apellido)

    # Primeros 3 dígitos del DNI
    primeros_digitos_dni = dni[:3]

    # Identificador final
    identificador = f"{primer_nombre}{letras_apellido}{primeros_digitos_dni}"
    return identificador


def validar_dni():
    while True:
        dni = input("Ingrese el DNI (7 u 8 dígitos): ").strip()

        if dni.isdigit() and len(dni) in (7, 8):
            return dni
        else:
            print("DNI inválido. Debe tener 7 u 8 dígitos. Intente de nuevo.")


# Programa principal
while True:
    nombre = input("Ingrese nombre completo del socio (o Enter para finalizar): ").strip()

    if nombre == "":
        print("Fin del registro de socios.")
        break

    dni = validar_dni()
    identificador = generar_identificador(nombre, dni)

    print("Identificador generado:", identificador)
    print("-" * 40)
