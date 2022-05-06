n = int(input())

contador = 0
qtd_pares = 0

while qtd_pares < n :
    if contador % 2 == 0:
        print(contador)
        qtd_pares += 1
    contador +=1
