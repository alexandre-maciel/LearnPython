# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

from math import cos, tan, sin, radians

angulo = float(input("insira o valor do angulo: "))

# precisamos transformar o angulo do prompt pra radial, se for o numero cru do prompt da errado no calculo do angulo.
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print(f"O cosseno de {angulo} é {cosseno:.2f}, sua tangente é {tangente:.2f} e o seno é {seno:.2f}")