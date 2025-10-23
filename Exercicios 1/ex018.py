'''

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


o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos, faça um programa que leia o nome dos quatro alunos e sorteie a ordem.

1) declara os alunos que vão participar
2) faz um sorteio para declarar qual a ordem de alunos para apresentar o trabalho

'''

import random

lista = [str(input("Quem é o primeiro aluno: ")), \
        str(input("Quem é o segundo aluno: ")), \
        str(input("Quem é o terceiro aluno: ")), \
        str(input("Quem é o quarto aluno: "))]


print (f"Os nomes a serem sorteados são: {lista}")

random.shuffle(lista)

print("A ordem de apresentação dos trabalhos ficou da seginte maneira: ")

print (lista)