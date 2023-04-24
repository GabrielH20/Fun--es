def converter_hora(horas,minutos):
    if horas<=12:
        turno = 'A.M'
    else:
        turno = 'P.M'
        horas-=12
    print(f'{horas}:{minutos} {turno}')
while True:
    digitar_horas = int(input('Digite aqui o valor das horas: '))
    digitar_minutos = int(input('Digite aqui o valor dos minutos'))

    converter_hora(digitar_horas,digitar_minutos)

    sair = input('Deseja sair do programa? [S] ou [N] : ').lower().startswith('s')

    if sair is True:
        print('Thanky you for converting hours with me')
        break
    else:
        print('Byebye')