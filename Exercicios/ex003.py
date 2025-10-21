# faça um programa que leia um numero inteiro e mostra na tela o seu sucessor e seu antecessor.

'''
preciso receber um numero
fazer uma variavel para o antecessor e um para o sucessor
'''

numero = int(input("Digite o número: "))

suc = numero + 1
ant = numero - 1

print (f"O número {numero} tem como seu antecessor o número {ant} e o seu sucessor o número {suc}")