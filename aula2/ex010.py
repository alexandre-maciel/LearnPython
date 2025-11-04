'''
10. Gerador de Lista (Usando list)
Objetivo: Praticar a criação de uma list e o uso de loops para preenchê-la.

Instruções:

Crie uma lista vazia chamada numeros_pares.

Use um loop for que itere de 2 até 20 (incluindo 20).

Dentro do loop, use o método .append() para adicionar o número atual à lista apenas se ele for par.

Ao final, imprima a lista numeros_pares.
'''

numeros_pares=[]

for i in range(2,21,2):
    numeros_pares.append(i)
print(numeros_pares)