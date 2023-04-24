def taxa_imposto(valor_item,valor_imposto):
    print(f'O item antes do imposto custa {valor_item}')
    print(f'Depois do imposto de {valor_imposto}% ficou {valor_item+(valor_item*(valor_imposto/100))}')
taxa_imposto(100,10)