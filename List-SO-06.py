#Exercícios
#Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

#Declaração de variáveis.

print ("Exercício 6")
x = input("Digite o valor de x: ")
y = input("Digite o valor de y: ")
print(f"\nAntes da troca: x = {x}, y = {y}")
x, y = y, x
print(f"Depois da troca: x = {x}, y = {y}")