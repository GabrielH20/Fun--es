lista_numeros = []

def exibir_sequencia(numero_digitado):
    contador = 0
    while True:
        if contador>=numero_digitado:
            break
        else:
            contador+=1
        lista_numeros.clear
        if len(lista_numeros)<=contador:
            lista_numeros.append(contador)
        print(lista_numeros)

exibir_sequencia(12)

print('-'*30)

lista_numeros = []

def exibir_numeros_dois(numero_digitado_dois):
    contador_dois=0
    while True:
        if contador_dois>=numero_digitado_dois:
            break
        else:
            contador_dois+=1
            lista_numeros.clear()
        for i in range(0,contador_dois,1):
            if len(lista_numeros)<contador_dois:
                lista_numeros.append(contador_dois)
        print(lista_numeros)

exibir_numeros_dois(12)
