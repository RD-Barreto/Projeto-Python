#Exercício 13
#Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

#Declaração de variáveis.

print ("Exercício 13")
quantidade = float(input("Digite a quantidade de alimento em kg: "))
consumo_diario = 0.05  # 50g convertido para kg 
dias = quantidade / consumo_diario
print ("O alimento durará aproximadamente: ", int (dias), "dias")
