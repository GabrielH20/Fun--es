def valor_pagamento(valor_parcela,dias_atraso):

    if dias_atraso==0:

        print(f'Parabéms vc é um ótimo cliente!\nPague o valor de {valor_parcela}')
    else:

        valor_multa_3_porct = valor_parcela*(3/100)
        valor_por_dia_atraso = valor_parcela*((dias_atraso/10)/100)
        valor_total_atrasado = valor_parcela + valor_multa_3_porct + valor_por_dia_atraso

        print('Infelizmente vc atrasou e terá que pagar uma multa :/')
        print(f'O valor será {valor_multa_3_porct}(3% da parcela) e {valor_por_dia_atraso}(0.1% por dia atrasdo) ')
        print(f'O valor total é de {valor_total_atrasado} R$')
        
valor_pagamento(100,100)