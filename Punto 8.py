def es_email_valido(email):
    return "@" in email


# Programa principal
email = input("Ingrese su dirección de email: ")

if es_email_valido(email):
    print("La dirección de email es válida.")
else:
    print("La dirección de email NO es válida.")
