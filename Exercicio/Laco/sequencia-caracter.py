def caracteres(n,m,c):
    linha = 0
    while linha < n:
        coluna = 0
        while coluna < m:
                print(c, end='')
                coluna += 1
        print()
        linha += 1
        
caracteres(10,15,'$')
