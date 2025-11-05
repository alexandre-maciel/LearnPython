'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

1) entrada de dados: quilometros a serem percorridos na viagem
2) criar uma condição na qual calcula o valor da viagem de acordo com a distancia percorrida

'''

quilometros = int(input("Quantos kilometros a serem percorridos: "))

valorViagem = 0

if quilometros > 200:
    valorViagem = quilometros * 0.45
    print(f"O valor da viagem custará R${valorViagem:.2f}")
else:
    valorViagem = quilometros *0.50
    print(f"O valor da viagem custará R${valorViagem:.2f}")
print("--Fim do Programa--")

