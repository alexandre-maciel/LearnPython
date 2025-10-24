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



# EXERCÍCIO 6: Tabuada do 5

print("--- Tabuada do 5 ---")

# O loop 'for' vai iterar com a variável 'i' de 1 até 10 (o 11 é exclusivo)
for i in range(1, 11):
    # Calcula o resultado da multiplicação: 5 * i
    resultado = 5 * i

    # Imprime a linha no formato "5 x i = resultado"
    # Usando f-string para facilitar a formatação
    print(f"5 x {i} = {resultado}")

print("--------------------")