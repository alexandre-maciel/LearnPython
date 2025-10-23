# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

# importa a biblioteca math para calcular os catetos e a hipotenusa 

import math

op = float(input("insira o valor do cateto oposto: "))
ad = float(input("insira o valor do cateto adjacente: "))
hipotenusa = math.hypot(op, ad)

print(f"O cateto oposto sendo {op} e o cateto adjacente {ad}, o valor da sua hipotenusa é {hipotenusa:.2f}")


