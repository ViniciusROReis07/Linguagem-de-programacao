n = int(input())

contator_repedicao = 0
contator_letras = 0
caracter = 65

if n > 0 and n <= 26 :
    while contator_repedicao < n :
        contator_letras = contator_repedicao+1
        for contator  in range(contator_letras) :
            print(chr(caracter),sep="",end="")
        print()
        caracter += 1
        contator_letras +=1
        contator_repedicao +=1
