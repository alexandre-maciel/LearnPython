# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

salario = int(input("insira o salario do funcionario: "))

aumento = salario*(15/100)

precofinal = salario + aumento

print(f"O aumento desse salario em 15% será de R${precofinal} reais")