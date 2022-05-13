salarios = []
qtd_salarios = int(input('Quantidade de salarios: '))
soma = 0

for _ in range(qtd_salarios):
    salario = float(input('Salário: R$ '))
    soma+= salario
    salarios.append(salario)

media = soma  / qtd_salarios

print(f'Média = R$ {media:.2f}')

for salario in salarios :
    if salario < media:
        print(f'Abaixo da média: R$ {salario:.2f}')
