'''
Verificador de Número Par ou Ímpar
Objetivo: Praticar operadores matemáticos (módulo %) e estruturas condicionais (if/else).

Instruções:

Peça ao usuário que digite um número inteiro.

Use o operador módulo (%) para verificar se o número é divisível por 2 (o resto da divisão por 2 é 0).

Se o resto for 0, imprima que o número é Par.

Caso contrário, imprima que o número é Ímpar.
'''

# recebo a entrada do usuário
n1 = int(input("Digite um número: "))

# crio uma condicional que faz a divisão e vê se o resto da divisão é 0 o que seria par e se não for, o número é impar
if n1 % 2 == 0:
    print (f"O número {n1} é par!")
else:
    print (f"O número {n1} é impar")