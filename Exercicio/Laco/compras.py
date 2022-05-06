credito = float(input("Seu crédito: "))

contador = 0
total_compra = 0
qtd_itens = 0
valor_total_tentativas = 0

while valor_total_tentativas<= credito  :
    contador += 1
    preco = float(input(f"Preço do item {contador}: "))
    if(total_compra+preco > credito):
        valor_total_tentativas += preco
        print(f"Compra do item {contador} negada!")
    else:
        total_compra+=preco
        valor_total_tentativas = total_compra
        qtd_itens+=1

credito -= total_compra

print(f"O total da compra é R$ {total_compra:.2f}")
print(f"Crédito restante é R$ {credito:.2f}")
    
