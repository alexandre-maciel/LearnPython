# faça um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça
# para o usuario tentar descobrir qual foi o numero escolhido pelo computador
# o programa deverá escrever se o usuario venceu ou perdeu

# 1) precisamos da entrada dos numeros de 0 a 5
# 2) precisamos utilizar alguma biblioteca para selecionar um numero
# 3) precisamos da entrada do dado do usuário entre 0 e 5
# 4) uma condicional que vai verificar se o numero do usuário é igual ao numero escolhido pelo programa

# importando a biblioteca random que faz a seleção de um numero aleatorio
import random

# utilizando o randrange(numeroinicial, numero final) para escolher um numero entre 0 e 5 e armazenando numa variavel
numeroEscolhido = random.randrange(1,5)

# pedindo um numero ao usuário
numeroUsuario = int(input("Escolha um número entre 1 e 5: "))

# fazendo a condicional que verifica se o numero do usuario é igual ao numero do programa
if numeroEscolhido == numeroUsuario:
    print("Parabéns! Você adivinhou o número!")
else:
    print(f"Você errou! Mais sorte na próxima vez! O número certo era o {numeroEscolhido}")

