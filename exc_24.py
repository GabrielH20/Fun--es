#Na matriz de 20x20 abaixo, quatro numeros ao longo de uma linha diagonal foram mar- ´
#cadas em negrito. O produto desses numeros ´ e 26 * 63* 78 * 14 = 1788696.
from copy import deepcopy
matriz = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,1,1,1],
    [1,1,1,1,1,1,2,1,1,1,1,1,1,4,1,4,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,2,20,2,2,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,20,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

def verificar_diagonal(matriz,invertida=False):
    salvar_valores_diagonais = []
    maior_valor_diagonal=1
    if invertida==True:
        for elemento in matriz:
            elemento.reverse()
    for elemento in matriz:
        for valor in elemento:

                multiplicador_valores_diagonais = 1

                indece_elemento = matriz.index(elemento)

                linha_valores_diagonais = []
                
                contador_diagonal = elemento.index(valor)

                try:
                    for i in range(indece_elemento,indece_elemento+4):
                        valor_diagonal = matriz[i][contador_diagonal]
                        multiplicador_valores_diagonais*=valor_diagonal
                        linha_valores_diagonais.append(valor_diagonal)
                        contador_diagonal+=1
                except:
                    continue

                if multiplicador_valores_diagonais>=maior_valor_diagonal:
                    maior_valor_diagonal=multiplicador_valores_diagonais
                    salvar_valores_diagonais=deepcopy(linha_valores_diagonais)
    if invertida==True:
        for elemento in matriz:
            elemento.reverse()
    if invertida==True:
        return f'Maior valor Multiplicado Diagonal Invertida: {maior_valor_diagonal}\nDos Diagonal Invertida:{salvar_valores_diagonais}\n'  
    else:
        return f'Maior valor Multiplicado Diagonal: {maior_valor_diagonal}\nDos Diagonal:{salvar_valores_diagonais}\n'                


def calcular_maior_valor_linha(matriz):
    #Variaveis Gerais para Salvar Principais valore
    salvar_elemento = 0

    #Variaveis de Valor Horizontal
    maior_valor_horizontal = 0
    salvar_valores_horizontais = []
   
    #Variaveis de Valor Vertical
    maior_valor_vertical = 0
    salvar_valores_verticais = []
    
    #Variaveis de valor Diagonal
    maior_valor_diagonal = 0
    salvar_valores_diagonais = []

    #Calcular Linhas
    for elemento in matriz:

        #Valores Horizontais
        for valor in elemento:

            multiplicar_valores_horizontais = 1
            indece_valor = elemento.index(valor)

            try:
                for i in range(indece_valor,indece_valor+4):
                    multiplicar_valores_horizontais*=elemento[i]
            except:
                continue

            if multiplicar_valores_horizontais>=maior_valor_horizontal:
                maior_valor_horizontal=multiplicar_valores_horizontais
                salvar_valores_horizontais = [elemento[i] for i in range(indece_valor,indece_valor+4)]

        #Valores Verticais
        for valor in elemento:

            multiplicar_valores_verticais = 1

            indece_elemento = matriz.index(elemento)
            indece_valor = elemento.index(valor)
            linha_valores_verticais = []

            try:
                for i in range(indece_elemento,indece_elemento+4):
                    valor_vertical = matriz[i][indece_valor]
                    multiplicar_valores_verticais*= valor_vertical
                    linha_valores_verticais.append(valor_vertical)
            except:
                continue

            if multiplicar_valores_verticais>=maior_valor_vertical:
                maior_valor_vertical=multiplicar_valores_verticais
                salvar_valores_verticais=deepcopy(linha_valores_verticais)

    

    print(f'Maior valor Multiplicado Horizontal: {maior_valor_horizontal}\nDos Valores Horizontais:{salvar_valores_horizontais}\n')
    print(f'Maior valor Multiplicado Vertical: {maior_valor_vertical}\nDos valores Verticais: {salvar_valores_verticais}\n')
    print(verificar_diagonal(matriz))
    print(verificar_diagonal(matriz,True))

calcular_maior_valor_linha(matriz)  



        