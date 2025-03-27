# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math

angulo = int(input("insira o valor do angulo: "))

cosseno = math.cos(angulo)
seno = math.sin(angulo)
tangente = math.tan(angulo)

print(f"O cosseno de {angulo} é {cosseno}, sua tangente é {tangente} e o seno é {seno}")