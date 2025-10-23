# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira. ex: digite um numero: 6.127. O numero 6.127 tem a porção inteira 6.

# recebe um numero real
# utilizando a função trunc para eliminar o valor após a virgula

import math

num = float(input("Digite um numero: "))

inteiro = math.trunc(num)

print(f"A porção inteira de {num} é {inteiro}")