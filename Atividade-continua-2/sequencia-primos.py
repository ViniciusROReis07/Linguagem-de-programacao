numero_inicial = int(input())
numero_final = int(input())

contator = numero_inicial

qtd_primos = 0

while contator <= numero_final:
    if contator != 1 :
        vezes_divido = 0
        for numero in range(2,contator):
            if contator%numero == 0 :
                vezes_divido = 1
                break;
                
        if vezes_divido == 0 :
            print(contator)
            qtd_primos+=1
    contator += 1

print(f'primos: {qtd_primos}')
