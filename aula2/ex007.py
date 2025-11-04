'''
7. Acumulador de Números (Loop while)
Objetivo: Praticar o loop while e acumulação de valores.

Instruções:

Crie uma variável chamada soma e inicialize-a com 0.

Use um loop while que continue pedindo ao usuário para digitar um número inteiro.

Se o usuário digitar 0, o loop deve ser interrompido (break).

A cada número digitado (que não seja 0), adicione-o à variável soma.

Ao final (depois que o usuário digitar 0), imprima o valor final da soma.
'''

# criar uma variavel soma
soma = 0

while True:
    adiciona = int(input("Digite um número para somar: "))
    soma = soma + adiciona
    print(soma)
    if adiciona == 0:
        break
print("fim da soma")
