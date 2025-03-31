# um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
print('\nSorteia 1 entre 4 alunos com solicitação para digitar seus nomes')
print('\nINSERÇÃO DE DADOS')

lista = str(input("Primeiro aluno: ")), \
        str(input("Segundo aluno: ")), \
        str(input("Terceiro aluno: ")), \
        str(input("Quarto aluno: "))

print(f'\nOs alunos a serem sorteados são: {lista}')

print(f"O aluno escolhido foi o {random.choice(lista)}")