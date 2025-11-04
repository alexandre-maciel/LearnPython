'''
import random

nome1 = str(input('  Digite o primeiro nome:     '))
nome2 = str(input('  Digiteo segundo nome:     '))
nome3 = str(input('  Digite o terceiro nome:     '))
nome4 = str(input('  Digite o quarto nome:     '))

lista = [nome1,nome2,nome3,nome4]

random.shuffle(lista)#shuffle significa embaralhar algo

print(lista)


fazer um programa que sorteia duplas 
'''

import random

nome1 = str(input("Primeiro nome: "))
nome2 = str(input("Segundo nome: "))
nome3 = str(input("Terceiro nome: "))
nome4 = str(input("Quarto nome: "))

lista = [nome1, nome2, nome3, nome4]

print (f'A lista de participantes é {lista}')

random.shuffle(lista)

print (f"A primeira dupla a ser sorteada é: ")

print(lista[0], lista[1])

print (f"A segunda dupla a ser sorteada é: ")

print(lista[2], lista[3])