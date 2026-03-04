#Exercício 5
#Receba os coeficientes A, B e C de uma equação do 2° grau (AX2+BX+C=0). Calcule e mostre
#as raízes reais (considerar que a equação possui 2 raízes reais).
print ("Exercício 5")
A = float ( input ("Coeficiente A: "))
B = float ( input ("Coeficiente B: "))
C = float ( input ("Coeficiente C: "))
soma = B ** 2 - 4 * A * C
raiz1 = (-B + soma ** 0.5) / (2 * A)
raiz2 = (-B - soma ** 0.5) / (2 * A)
print ("Raiz 1: ", (raiz1))
print ("Raiz 2: ", (raiz2))