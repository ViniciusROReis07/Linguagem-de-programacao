ano_inicio = int(input())
ano_fim = int(input())

anos_bissextos = 0
contator = ano_inicio

while contator <= ano_fim :
    if (contator%4 == 0 and contator%100 != 0 ) or contator%400 == 0  :
        anos_bissextos += 1
        print(contator)
    contator += 1
print(f'bissextos: {anos_bissextos}')
