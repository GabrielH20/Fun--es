#Nesse projeto iremos criar um gerenciamento de um dicionario com noivos
#Será feito um crud simples (Adicionar,Excluir,Ler e Atuazliar)
#Tenterá ser  feito as práticas do CLean Code   
from os import system
from copy import deepcopy

lista_noivos = [
    {'nome':'Gabriel','sobrenome':'Henrique','idade':20,'sexo':'M','id_noivo':1},
    {'nome':'Ninguem','sobrenome':'Sou_Sozinho','idade':200,'sexo':'BCT','id_noivo':1},
    {'nome':'Zadoque','sobrenome':'Teófilo','idade':18,'sexo':'M','id_noivo':2},
    {'nome':'Leticia','sobrenome':'Sla_O_Sobrenome','idade':19,'sexo':'F','id_noivo':2},
]

linha = '-'*25

#->lISTA DE FUNÇÕES USADAS EM TODO O CÓDIGO<-
#Exibir lista de noivos
def exibir_noivos(lista_noivos):
    print(linha)
    for valor in lista_noivos:

        for chave,elemento in valor.items():

            print(f'{chave} : {elemento}',end=' / ')
        print('')
    print(linha)
    
#Checar se quer continuar na operação
def checar_continuar_na_operacao(nome_operacao):

    opcao_sair = input(f'Deseja sair da operação {nome_operacao}? [s] ou [n]\nDigite aqui: ').lower().startswith('s')

    if opcao_sair==True:
        print('Adeus!')
    else:
        print(f'Então vamos continuar {nome_operacao}!')
    
    return opcao_sair

#Limpar terminal do python
def limpar_terminal():
    system('cls')

#Checar se o ID existe na lista de noivos
def checar_e_exibir_id_noivos(lista_noivos,valor_id_excluir):

    contador_noivos = 0

    print(linha)
    for noivo in lista_noivos:

        if valor_id_excluir==noivo['id_noivo']:

            for chave,valor in noivo.items():

                print(f'{chave} : {valor}',end=' / ')
                contador_noivos+=1
            print()

    return contador_noivos

#->FUNÇÕES USADAS NO ADICIONAR NOIVOS<-
#Adicionar novos noivos a lista de noivos
def adicionar_noivos(lista_noivos):
    while True:
        guardar_noivos_adicionar = []

        adicionar_id_noivo = definir_proximo_id(lista_noivos)

        quantidade_noivos_adicionar = int(input('Digite aqui o número de noivos que deseja adicionar: '))

        if quantidade_noivos_adicionar<=0 or quantidade_noivos_adicionar>=5:
            return 'Infelizmente digitou um número inválido!'
        
        for i in range(quantidade_noivos_adicionar):
            print(f'{linha}\nNoivo {i+1} / {quantidade_noivos_adicionar}')
            
            adicionar_nome_noivo = input('Digite aqui o Primeiro nome do noivo: ')

            adicionar_sobrenome_noivo = input('Digite aqui o Sobrenome do noivo: ')

            adicionar_idade_noivo = int(input('Digite aqui a Idade do noivo: '))

            adicionar_sexo_noivo = input('Digite aqui o Sexo do noivo: ')

            if checar_comprimindo_infos_noivo(adicionar_nome_noivo,adicionar_idade_noivo,adicionar_sexo_noivo)==False:
                return 'Infelizmente algum valor não foi preenchido'
            
            if validar_dados_noivos(adicionar_nome_noivo,adicionar_sobrenome_noivo,adicionar_idade_noivo,adicionar_sexo_noivo)==True:

                guardar_noivos_adicionar.append({'nome':adicionar_nome_noivo,'sobrenome':adicionar_sobrenome_noivo,'idade':adicionar_idade_noivo,'sexo':adicionar_sexo_noivo.upper(),'id_noivo':adicionar_id_noivo})

            else:
                return 'Valores do noivo infelizmente estão incorretos, ou ele(a) é muito novo!'
        
        for noivo_adicionar in guardar_noivos_adicionar:
            lista_noivos.append(noivo_adicionar)

        exibir_noivos(lista_noivos)

        if checar_continuar_na_operacao('Adicionando')==True:
            break

        limpar_terminal()

def checar_comprimindo_infos_noivo(*args):

    for valor in args:
        if len(str(valor))==0:
            return False
    return True

#Checa se todos os dados são válidos, ou se tem algum tipo de dado errado
def validar_dados_noivos(adicionar_nome_noivo,adicionar_sobrenome_noivo,adicionar_idade_noivo,adicionar_sexo_noivo):
    
    
    if len(separar_nomes(adicionar_nome_noivo))!=1:
        return False
    
    elif len(separar_nomes(adicionar_sobrenome_noivo))!=1:
        return False
    
    elif adicionar_idade_noivo<=17:
        return False
    
    elif len(adicionar_sexo_noivo)>3:
        return False
    
    else:
        return True
    
def separar_nomes(string_separar):

    separar_nome = string_separar.split(' ')
    return separar_nome

def definir_proximo_id(lista_noivos):

    valor_final = lista_noivos[-1]
    return valor_final['id_noivo'] + 1

#->FUNÇÕES USADAS NO EXCLUIR NOIVOS<-
#Adicionar novos noivos a lista de noivos
def excluir_noivos(lista_noivos):
    while True:
        
        exibir_noivos(lista_noivos)

        valor_id_excluir = int(input('Digite aqui o valor do ID que deseja excluir: '))

        if checar_e_exibir_id_noivos(lista_noivos,valor_id_excluir)==0:

            return 'Infelizmente o ID digitado não existe no nosso banco de dados!'

        print(linha)
        confirmacao_excluir_noivos = input(f'Esses são os noivos de ID {valor_id_excluir}, deseja exclui-los? [s] ou [n]\nDigite aqui: ').lower().startswith('s')
        print(linha)

        if confirmacao_excluir_noivos==True:

            excluir_noivos_confirmacao(lista_noivos,valor_id_excluir)

            print('A lista após as alterações: ')
            exibir_noivos(lista_noivos)
        
        if checar_continuar_na_operacao('Excluindo')==True:
            break
        limpar_terminal()
        
    limpar_terminal()


def excluir_noivos_confirmacao(lista_noivos,valor_id_excluir):
    
    #Infelizmente não consigo excluir todos os noivos do id de uma vez,
    #Então ele pecorre a lista diversas vezes garantindo que todos do ID valor_id_excluir sejam excluidos
    for i in range(len(lista_noivos)):
        for noivo in lista_noivos:
            if noivo['id_noivo']==valor_id_excluir:
                lista_noivos.remove(noivo)
    
def atualizar_noivos(lista_noivos):
    while True:

        exibir_noivos(lista_noivos)

        nome_sobrenome_atualizar = input('Digite o nome e sobrenome de quem deseja atualizar: ')

        salvar_indece_atualizacao = validar_nome_sobrenome_atualizacao(nome_sobrenome_atualizar)

        if isinstance(salvar_indece_atualizacao,bool):
            return 'Infelizmente não encontramos alguem com esse nome no banco de dados!'        

        while True:
            
            print(linha)
            exibir_chaves(salvar_indece_atualizacao)

            escolher_valor_atualizar = input('Digite aqui o valor que deseja alterar:  ')

            if checar_chaves_existentes(escolher_valor_atualizar)==False:
                return 'Infelizmente digitou uma chave inválida!'

            salvar_tipo_atualizar = type(lista_noivos[salvar_indece_atualizacao][escolher_valor_atualizar])

            valor_atualizacao = input('Digite aqui o novo valor: ')

            if escolher_valor_atualizar=='idade':
                try:
                    valor_atualizacao = int(valor_atualizacao)
                except:
                    return 'Infelizmente digitou um outro dado inves de número'
                
            if isinstance(valor_atualizacao,salvar_tipo_atualizar):

                noivo_atualizar_guardar = deepcopy(lista_noivos[salvar_indece_atualizacao])

                noivo_atualizar_guardar[escolher_valor_atualizar] = valor_atualizacao

                if validar_dados_noivos(noivo_atualizar_guardar['nome'],noivo_atualizar_guardar['sobrenome'],noivo_atualizar_guardar['idade'],noivo_atualizar_guardar['sexo'],):
                    lista_noivos.remove(lista_noivos[salvar_indece_atualizacao])
                    lista_noivos.insert(salvar_indece_atualizacao,noivo_atualizar_guardar)
                else:
                    return 'Infelizmente digitou um valor inválido!'

            for chave,valor in lista_noivos[salvar_indece_atualizacao].items():
                print(f'{chave} : {valor}',end=' / ')
            print()

            if checar_continuar_na_operacao('Alterando esse noivo')==True:
                break
            
            limpar_terminal()

        if checar_continuar_na_operacao('Atualizando outros noivos')==True:
            break

        limpar_terminal()

#Criar uma função para exibir ids específicos
def validar_nome_sobrenome_atualizacao(nome_sobrenome):

    nome_validar,sobrenome_validar = dividir_nome = deepcopy(separar_nomes(nome_sobrenome))

    for noivo in lista_noivos:

        if nome_validar==noivo['nome'] and sobrenome_validar==noivo['sobrenome']:

            salvar_index = lista_noivos.index(noivo)
            return salvar_index
        
    return False

def exibir_chaves(indece):

    for chave in lista_noivos[indece].keys():
        if chave=='id_noivo':
            break
        print(f'{chave} : {lista_noivos[indece][chave]}')

def checar_chaves_existentes(escolher_valor_atualizar):

    for valor in lista_noivos[0].keys():
        if escolher_valor_atualizar==valor:
            break
    else:
        return False
        
while True:
    tipo_operacao = input('Digite aqui o tipo de operacao que deseja:')

    if tipo_operacao=='Adicionar':
        adicionar_noivos(lista_noivos)
    elif tipo_operacao=='Exibir':
        exibir_noivos(lista_noivos)
    elif tipo_operacao=='Excluir':
        excluir_noivos(lista_noivos)
    elif tipo_operacao=='Atualizar':
        atualizar_noivos(lista_noivos)
    else:
        print('Digitou um valor inválido tente novamente!')
        continue

    if checar_continuar_na_operacao('Menu Principal'):
        break

    limpar_terminal()