'''
Escreva um programa que pergunte o salário de um Funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

1) entrada do valor do salario
2) utilizar uma condicional para verificar os parametros
3) fazer o calculo do novo salario
'''

salarioAtual = int(input("Qual é o salario atual: "))

aumentoDez = 10/100

aumentoQuinze = 15/100

novoSalario = 0

aumento = 0

if salarioAtual > 1250:
    aumento = salarioAtual * aumentoDez
    novoSalario = salarioAtual + aumento
    print(f"O salário de R${salarioAtual:.2f} passa a ser de R${novoSalario:.2f} com o aumento de 10%(R${aumento:.2f})")
else: 
    aumento = salarioAtual * aumentoQuinze
    novoSalario = salarioAtual + aumento
    print(f"O salário de R${salarioAtual:.2f} passa a ser de R${novoSalario:.2f} com o aumento de 15%(R${aumento:.2f})")
