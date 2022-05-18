def busca_indexs(valor, sequencia):
    lista_indexs = []
    
    for i, item in enumerate(sequencia):
        if item == valor:
            lista_indexs.append(i)
    if len(lista_indexs) < 0 :
        return -1
    else :
        return lista_indexs

lista = [3, 6, 5, 8, 0, 8, 2]

indexs = busca_indexs(8,lista)

print(indexs);
