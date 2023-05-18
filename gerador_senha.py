from string import ascii_lowercase
from random import choice

lista_pessoas_senhas = ['Gabriel','Zadoque','Matheus','Maria','Felipe','Kayle']

lista_alfabeto = [letra for letra in ascii_lowercase]
senhas_pessoas = []

def definir_quantidade_elementos(tamanho):
    return choice(range(0,round(tamanho/3)))

def gerar_senhas(lista_nomes,tamanho_senha_max=9,conter_numeros=False,conter_caracteres_especiais=False,conter_letras_maisculas=False):
    

    for nome in lista_nomes:

        lista_condicoes = []
        condicao=0
        senha_caracteres=[]
        
        for i in range(0,tamanho_senha_max):

            aleatorizar_tamanho = choice([1,2])

            if aleatorizar_tamanho==2 and conter_letras_maisculas==True:
                senha_caracteres.append(choice(lista_alfabeto).upper())
            if aleatorizar_tamanho==1 or conter_letras_maisculas==False:
                senha_caracteres.append(choice(lista_alfabeto))
        
        if conter_numeros==True:


            for i in range(0,2):

                senha_caracteres.insert(choice(range(0,len(senha_caracteres))),str(choice(range(9))))
                condicao+=1

        caracteres = ['&','$','#','@','_','*']
        if conter_caracteres_especiais==True:


            for i in range(0,2):

                senha_caracteres.insert(choice(range(0,len(senha_caracteres))),choice(caracteres))
                condicao+=1
        
        print(condicao,senha_caracteres,lista_condicoes)
        while (condicao!=0):

            remover_elemento = (choice(range(0,len(senha_caracteres))))

            print(remover_elemento,senha_caracteres[remover_elemento])
        
            if isinstance(senha_caracteres[remover_elemento],int) or senha_caracteres[remover_elemento] in caracteres:
                continue
            
            senha_caracteres.remove(senha_caracteres[remover_elemento])
            condicao-=1

        senha = ''

        for elemento in senha_caracteres:
            senha+=elemento
        senhas_pessoas.append({nome:senha})

    for valor in senhas_pessoas:
        for pessoa,senha_2 in valor.items():
            print(f'{pessoa} : {senha_2}')
gerar_senhas(lista_pessoas_senhas,9,True,True,True)

        