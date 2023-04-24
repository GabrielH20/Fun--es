import random

lista_scrab = [2,3,12]
lista_win = [7,11]
lista_ponto = [4,5,6,8,9,10]

def aleatorio():

    valor_um = random.randint(1,6)
    valor_dois = random.randint(1,6)
    return (valor_um + valor_dois)

def scrab():

    salvar_aleatorio = aleatorio()

    print('O número que vc tirou foi',salvar_aleatorio)
    if salvar_aleatorio in lista_win:
        return 'Parabens vc Ganhou'
    if salvar_aleatorio in lista_scrab:
        return 'Infelizmente vc perdeu'
    print(f'Vc fez um ponto!({salvar_aleatorio}),tente tirar outro para ganhar!')

    ponto()
    
def ponto():

    while True:

        salvar_aleatorio = aleatorio()
        
        input(f'Vc tirou {salvar_aleatorio},clique para continuar')
        if salvar_aleatorio in lista_ponto:
            print ('Vc fez um ponto vc ganhou!')
        elif salvar_aleatorio == 7:
            print('Infelizmente vc tirou 7 e perdeu :/')
        else:
            print('Opa ainda tem esperanças')
            continue
        break
    
v2 = scrab()
print(v2)