dia = input()
dias_para_entrega = int(input())

dias_semana = ['domingo','segunda','terca','quarta','quinta','sexta','sabado']

dia_entrega = ''

if dias_para_entrega == 0:
    print('chega hoje!')
else:
    contator_laco = 0
    index_dia = dias_semana.index(dia) 
    tamanho_lista = len(dias_semana) - 1

    while(True):
        if contator_laco == dias_para_entrega :  
            dia_entrega = dias_semana[index_dia]
            break;
        else:
            if index_dia == tamanho_lista:
                index_dia = 0
            else:
                index_dia += 1

        contator_laco+=1

    print('sera entregue',dia_entrega) 
        
    
    
