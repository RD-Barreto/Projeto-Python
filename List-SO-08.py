#Exercícios
#Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.

#Declaração de variáveis.

print ("Exercício 8")
deposito = float(input("Digite o valor do depósito: "))
rendimento = deposito * 0.013  # 1,3% convertido para decimal
valor_final = deposito + rendimento
print ("Valor após 1 mês de aplicação: ", valor_final)