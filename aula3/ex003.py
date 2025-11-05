'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR


1) entrada de um numero inteiro
2) verificação com condicional utilizando modulo

'''

numero = int(input("Digite o número: "))

if numero % 2 == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O número {numero} é impar")