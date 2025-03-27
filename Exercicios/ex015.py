# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math

op = int(input("insira o valor do cateto oposto: "))
ad = int(input("insira o valor do cateto adjacente: "))

calc = op + ad

hipotenusa = math.sqrt(calc)

print(f"O cateto oposto sendo {op} e o cateto adjacente {ad}, o valor da sua hipotenusa é {math.trunc(hipotenusa)}")


