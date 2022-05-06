numero = int(input())

numero_impar =  numero
numero_par = numero

while(True):
    numero_impar-=1
    if numero_impar%2 == 1:
        break

while(True):
    numero_par+=1
    if numero_par%2 == 0:
        break
    
print(numero_impar,numero_par)
