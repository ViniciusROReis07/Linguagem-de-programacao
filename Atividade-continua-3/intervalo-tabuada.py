a = int(input())
b = int(input())

if a <= b :
    for multiplicador in range (a,b+1) :
        
        for numero in range(1,11):
            multiplicacao = multiplicador*numero
            print(f'{multiplicador} x {numero} = {multiplicacao}')
        print('----------')
else :
    print('Nenhuma tabuada no intervalo!')
