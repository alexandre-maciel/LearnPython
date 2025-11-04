'''
2. Calculadora de Soma Simples
Objetivo: Praticar conversão de tipos (string para número) e operações aritméticas básicas.

Instruções:

Peça ao usuário que digite dois números inteiros.

Armazene-os em variáveis. Lembre-se: a função input() retorna strings, então você precisará convertê-los para inteiros (int()).

Calcule a soma dos dois números.

Imprima o resultado na tela com uma mensagem clara.

'''

# A entrada do primeiro dado
numero1 = int(input("Digite o primeiro número: "))

# Entrada do segundo dado
numero2 = int(input("Digite o segundo número: "))

# criar a variavel que faz a soma dos números fornecidos pelo usuário
soma = numero1+numero2

# mostrando na tela o valor de resultado
print(f"A soma de {numero1} + {numero2} é igual a {soma}")