# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos, faça um programa que leia o nome dos quatro alunos e sorteie a ordem.

import random

print('Sorteia a ordem em que os alunos vão se apresentar')

lista = input('Primeiro aluno: '), \
        input('Segundo aluno: '), \
        input('Terceiro aluno: '), \
        input('Quarto aluno: ')

print(f'\nOs alunos que vão se apresentar são {lista}')

print (f'A ordem de apresentação dos trabalhos é: ')

random.shuffle(lista)

print(lista)