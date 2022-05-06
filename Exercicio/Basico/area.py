A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)

area_triangulo_retangulo = "{:.3f}".format((A*C)/2)

area_circulo = "{:.3f}".format(3.14159*(C**2))

area_trapezio = "{:.3f}".format(((A+B)*C)/2)

area_quadrado = "{:.3f}".format(B**2)

area_retangulo = "{:.3f}".format(A*B)

print("TRIANGULO:",area_triangulo_retangulo)
print("CIRCULO:",area_circulo)
print("TRAPEZIO:",area_trapezio)
print("QUADRADO:",area_quadrado)
print("RETANGULO:",area_retangulo)
