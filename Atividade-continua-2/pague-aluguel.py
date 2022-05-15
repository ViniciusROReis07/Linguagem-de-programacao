total_divida = int(input())
valor_mensal = int(input())
contator = 1
valor_restante = total_divida

while valor_restante  > 0 :
    print(f'pagamento: {contator}')
    print(f'antes = {valor_restante}')
    valor_restante -= valor_mensal
    if valor_restante < 0 :
        print('depois = 0')
    else :
        print(f'depois = {valor_restante}')
    contator += 1
    print('-----')
