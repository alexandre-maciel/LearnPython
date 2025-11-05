'''

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

'''

# Importa a função isleap da biblioteca calendar

ano = int(input("Que ano você quer analisar? "))

if ano % 4 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")