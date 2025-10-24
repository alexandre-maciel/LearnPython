'''
6. Tabuada
Objetivo: Praticar o loop for e operações dentro do loop.

Instruções:

Use um loop for que itere de 1 a 10.

Dentro do loop, calcule e imprima o resultado da multiplicação de 5 pelo número atual da iteração.

Declarar um número dado pelo usuário
Começar um multiplicador em 0 e ir somando +1
'''

numero = int(input("Qual é o número: "))
mult = 0

while (mult <= 10):
    conta = numero * mult
    print(f"{numero}x{mult}={conta}")
    mult = mult + 1
print ('Fim da Tabuada')