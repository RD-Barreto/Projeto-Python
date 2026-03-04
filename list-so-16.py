#Exercícios

#Declaração de variáveis.

h_trabalhada = float (input("Digite o número de horas trabalhadas: "))
perc_descont = float (input("Digite o percentual de desconto: "))

salario_bruto = h_trabalhada * 10
print ("Salário bruto: ", salario_bruto)
desconto = salario_bruto * (perc_descont / 100)
salario_liquido = salario_bruto - desconto
print ("Salário líquido: ", salario_liquido)
dependentes = int (input("Digite o número de dependentes: "))
salario_final = salario_liquido + (dependentes * 100)
print ("Salário final: ", salario_final)
