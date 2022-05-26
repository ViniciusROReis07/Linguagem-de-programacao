lista_valores = []
exibicoes = []

while True:
    dados = input()
    valor1 = dados.split(' ')[0]
    if dados != '' and dados != 'exibir' and dados != 'encerrar' and valor1 != 'remover' and valor1 != 'adicionar':
        valores = dados.split(' ')
        for valor in valores :
            lista_valores.append(int(valor))
            lista_valores.sort(key=int)
    elif dados == 'exibir':
        for valor in lista_valores :
            print(valor,sep='',end=' ')
        print()
    elif dados == 'encerrar':
        for valor in lista_valores :
            print(valor,sep='',end=' ')
        break
    elif valor1 == 'remover':
        resultado = ''
        valor_buscado = int(dados.split(' ')[1])
        for valor in lista_valores:
            if valor == valor_buscado :
                resultado = valor
                lista_valores.pop(lista_valores.index(valor))
                break
        
        if resultado == '':
            print(f'código {valor_buscado} não encontrado')
            print()
            
    elif valor1 == 'adicionar':
        lista_valores.append(int(dados.split(' ')[1]))
        lista_valores.sort(key=int)

