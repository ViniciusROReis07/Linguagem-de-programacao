preco_mercadoria = float(input())
quantidade = int(input())

desconto_total = (preco_mercadoria*10)/100
valor_total = preco_mercadoria*quantidade

for desconto in range(quantidade):
    desconto_total += (desconto_total*1)/100

print(desconto_total)
    
print(valor_total)
print(valor_total - desconto_total)
    
