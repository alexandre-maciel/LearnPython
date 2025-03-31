# o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos, faça um programa que leia o nome dos quatro alunos e sorteie a ordem.

import random

print('Sorteia a ordem em que os alunos vão se apresentar')

a1 = input('\nPrimeiro aluno: ')
a2 = input('\nSegundo aluno: ')
a3 = input('\nTerceiro aluno: ')
a4 = input('\nQuarto aluno: ')

lista = [a1, a2, a3, a4]

print(f'\nOs alunos que vão se apresentar são {lista}')

print (f'\n A ordem de apresentação dos trabalhos é: ')

random.shuffle(lista)

print(lista)