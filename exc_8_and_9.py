lista_numero = []
def avaliar_numero(numero_digitado):
    numero_string = str(numero_digitado)

    print(f'O número tem {len(numero_string)} digitos')

    #Para inverter textos
    print(numero_string[::-1])

avaliar_numero(123234143214)