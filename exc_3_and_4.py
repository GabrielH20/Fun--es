def soma(valor_um_soma=None,valor_dois_soma=None,valor_tres_soma=None):

    lista_valores_somas = [valor_um_soma,valor_dois_soma,valor_tres_soma]

    if None in lista_valores_somas:

        print('Infelizmente vc não digitou algum dos valores!')

    else:

        print(f'{valor_um_soma} + {valor_dois_soma} + {valor_tres_soma} =',end=' ')

        resposta_soma = valor_um_soma+valor_dois_soma+valor_tres_soma
        print(f'{resposta_soma}')

        if resposta_soma%2==0:
            print('Valor positivo!')
        else:
            print('Valor negativo')

soma(10,17,0)