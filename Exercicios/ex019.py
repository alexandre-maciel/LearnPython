import random

nome1 = str(input('  Digite o primeiro nome:     '))
nome2 = str(input('  Digiteo segundo nome:     '))
nome3 = str(input('  Digite o terceiro nome:     '))
nome4 = str(input('  Digite o quarto nome:     '))

lista = [nome1,nome2,nome3,nome4]

random.shuffle(lista)#shuffle significa embaralhar algo

print(lista)