'''
9. Classificador de Faixa Etária
Objetivo: Praticar estruturas condicionais aninhadas (if, elif, else).

Instruções:

Peça ao usuário que digite uma idade (número inteiro).

Use condicionais para classificar a pessoa nas seguintes faixas:

Se a idade for menor que 13: Imprima "Criança".

Se a idade estiver entre 13 e 18 (incluindo 13 e 18): Imprima "Adolescente".

Se a idade for maior que 18: Imprima "Adulto".
'''

idade = int(input("Qual a sua idade? "))

if idade <= 13:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
else:
    print('Adulto')