#Fac¸a um programa para determinar a proxima jogada em um Jogo da Velha. Assumir que ´
#o tabuleiro e representado por uma matriz de 3 x 3, onde cada posic¸ ´ ao representa uma ˜
#das casas do tabuleiro. A matriz pode conter os seguintes valores -1, 0, 1 representando
#respectivamente uma casa contendo uma pec¸a minha (-1), uma casa vazia do tabuleiro
#(0), e uma casa contendo uma pec¸a do meu oponente (1).
from random import randint
matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
ia_jogada = 0

def exibir_jogo_da_velha(matriz):
    for elemento in matriz:
        for valor in elemento:
            print(valor,end='  ')
        print()
    print('-'*30)

def usuario_jogar(matriz):
    while True:
        try:
            linha_jogar = int(input('Digite aqui a linha:'))
            coluna_jogar = int(input('Digite aqui a coluna: '))
            print('-'*30)
            if linha_jogar>len(matriz) or coluna_jogar>len(matriz[0]):
                print('Infelizmente digitou um valor inválido! Tente novamente')
                continue
            if matriz[linha_jogar][coluna_jogar] not in [-1,1]:
                matriz[linha_jogar].pop(coluna_jogar)
                matriz[linha_jogar].insert(coluna_jogar,-1)
                exibir_jogo_da_velha(matriz)
            else:
                print('Tente outro valor não ocupado!')
                continue
            break
        except:
            print('Valor fora do range! ou não inteiro!')
            continue

def setar_elemento(elemento):
    set_elemento = set(elemento)
    if len(set_elemento)==1 and 0 not in set_elemento:
        if -1 in set_elemento:
            jogador = 'Jogador(-1)'
        else:
            jogador = 'Máquina(1)'
        print(f'O jogador {jogador} ganhou')
        return True
    
def inverter_matriz(matriz):
    for elemento in matriz:
        elemento.reverse()

def checar_diagonal(matriz,invertida=False):
    if invertida==True:
        inverter_matriz(matriz)
    contador = 0
    linha_dois = []
    for i in range(3):
        linha_dois.append(matriz[i][contador])
        contador+=1
    if invertida==True:
        inverter_matriz(matriz)
    return linha_dois

def checar_vitoria(matriz_jogo_da_velha):
    #Checar vitória Horizontal
    for elemento in matriz_jogo_da_velha:
        if setar_elemento(elemento)==True:
            return True
    #Checar vitória Vertical
    for i in range(3):
        linha = []
        for k in range(3):
            linha.append(matriz_jogo_da_velha[k][i])
        if setar_elemento(linha)==True:
            return True
    #Checar Diagonal
    if setar_elemento(checar_diagonal(matriz_jogo_da_velha,False))==True:
        return True
    #Checar Diagonal Invertida
    if setar_elemento(checar_diagonal(matriz_jogo_da_velha,True))==True:
        return True

def adicionar_valor_horizontal(linha):
    for indece,valor in enumerate(linha):
        if valor==0:
            del linha[indece]
            linha.insert(indece,1)

def adicionar_valor_diagonal_vertical(matriz_jogo_da_velha,local_linha,local_coluna):
    global ia_jogada
    del matriz_jogo_da_velha[local_linha][local_coluna]
    matriz_jogo_da_velha[local_linha].insert(local_coluna,1)
    ia_jogada+=1

def inverter_matriz(matriz):
    for elemento in matriz:
        elemento.reverse()
        
def checar_valor_diagonal(matriz_jogo_da_velha,invertido=False):
    global ia_jogada
    if invertido==True:
       inverter_matriz(matriz_jogo_da_velha)
    for valor in [1,-1]:
        linha= []                
        valor_coluna=0
        contador_diagonal = 0
        for i in range(3):
            valor_diagonal = matriz_jogo_da_velha[i][valor_coluna]
            if valor_diagonal==valor:
                contador_diagonal +=1

            if valor_diagonal==0:
                salvar_localizacao_i = i
                salvar_localizacao_contador = valor_coluna

            valor_coluna+=1

        if contador_diagonal==2 and ia_jogada==0:
            adicionar_valor_diagonal_vertical(matriz_jogo_da_velha,salvar_localizacao_i,salvar_localizacao_contador)
            ia_jogada+=1
    if invertido==True:
       inverter_matriz(matriz_jogo_da_velha)
       
def randomizar_jogada_maquina(matriz_jogo_da_velha):
    while True:
        valor_coluna_aleatorio = randint(0,2)
        valor_linha_aleatorio = randint(0,2)
        if matriz_jogo_da_velha[valor_linha_aleatorio][valor_coluna_aleatorio]==0:
            adicionar_valor_diagonal_vertical(matriz_jogo_da_velha,valor_linha_aleatorio,valor_coluna_aleatorio)
            break
        else:
            continue

def maquina_jogar(matriz_jogo_da_velha):
    global ia_jogada
    ia_jogada=0
    #Marcar IA horizontal
    for linha in matriz_jogo_da_velha:
        for valor in [1,-1]:
            valor_coluna=0
            for elemento in linha:
                if elemento==valor:
                    valor_coluna+=1
            if valor_coluna==2 and ia_jogada==0:
                adicionar_valor_horizontal(linha)
                ia_jogada+=1
    #Marcar IA vertical
    for valor in [1,-1]:
        for i in range(3):
            linha_vertical = []
            valor_coluna = 0
            for k in range(3):
                if valor==matriz_jogo_da_velha[k][i]:
                    valor_coluna+=1
                else:
                    salvar_localizacao_k = k
                    salvar_localizacao_i = i
            if valor_coluna==2 and ia_jogada==0:
                adicionar_valor_diagonal_vertical(matriz_jogo_da_velha,salvar_localizacao_k,salvar_localizacao_i)
                break
    #Marcar IA diagonal
    checar_valor_diagonal(matriz_jogo_da_velha)
    #Marcar IA diagonal invertida
    checar_valor_diagonal(matriz_jogo_da_velha,True)
    if ia_jogada==0:
        randomizar_jogada_maquina(matriz_jogo_da_velha)
    exibir_jogo_da_velha(matriz_jogo_da_velha)

def checar_velha(matriz):
    contador = 0
    for elemento in matriz:
        if 0 not in elemento:
            contador+=1
    if contador==3:
        print('Infelizmente o jogo deu velha!')
        return True
    else:
        return False
    
while True:
    usuario_jogar(matriz)
    if checar_vitoria(matriz)==True or checar_velha(matriz)==True:
        break
    maquina_jogar(matriz)