def busca_linear(valor, sequencia):
    for i, item in enumerate(sequencia):
        if item == valor:
            return i
    return -1

lista = [3, 6, 5, 8, 0, 8, 2]

index = busca_linear(8,lista)

print(index);
