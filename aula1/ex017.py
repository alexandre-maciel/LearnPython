# um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

'''
1) Primeiramente preciso fazer a entrada dos 4 alunos numa lista
2) importar a função random para sortear um nome dentre uma lista
'''

import random

lista = str(input("Quem é o primeiro aluno: ")), \
        str(input("Quem é o segundo aluno: ")), \
        str(input("Quem é o terceiro aluno: ")), \
        str(input("Quem é o quarto aluno: "))

print (f"Os nomes a serem sorteados são: {lista}")

print(f"O aluno escolhido foi o {random.choice(lista)}")







# import random
# print('\nSorteia 1 entre 4 alunos com solicitação para digitar seus nomes')
# print('\nINSERÇÃO DE DADOS')

# lista = str(input("Primeiro aluno: ")), \
#         str(input("Segundo aluno: ")), \
#         str(input("Terceiro aluno: ")), \
#         str(input("Quarto aluno: "))

# print(f'\nOs alunos a serem sorteados são: {lista}')

# print(f"O aluno escolhido foi o {random.choice(lista)}")