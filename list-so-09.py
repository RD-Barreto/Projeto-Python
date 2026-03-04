#Exercícios 
#Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.

#Declaração de variáveis.

print ("Exercício 09")
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
quadrado1 = int(num1) ** 2
quadrado2 = int(num2) ** 2  
soma_quadrados = quadrado1 + quadrado2
print(f"\nO quadrado de {num1} é: {quadrado1}")
print(f"O quadrado de {num2} é: {quadrado2}")
print ("A soma dos quadrados é: ", soma_quadrados)  