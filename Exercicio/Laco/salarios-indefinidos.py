salarios = []
soma = 0
contador = 0

while True:
    salario = float(input('Salário: R$ '))
    if(salario == -1):
        break
    
    soma+= salario
    contador += 1
    salarios.append(salario)

    
if contador>0 : 
    media = soma  / contador

    print(f'Média = R$ {media:.2f}')

    for salario in salarios :
        if salario < media:
            print(f'Abaixo da média: R$ {salario:.2f}')
