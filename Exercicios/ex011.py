# faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
'''
1) receber o valor do salario atual do funcionario
2) calcular o aumento com base no atual salario
3) somar o salario atual com o aumento
4) mostrar o resultado do novo salario do funcionario
'''

salario = float (input ("Salario atual do funcionario: "))

aumento = salario * (15/100)

novosalario = salario + aumento

print (f"O salario passa de R${salario:.2f} para R${novosalario:.2f} com o aumento de 15% que equivale a R${aumento:.2f}")