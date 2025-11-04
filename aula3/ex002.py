'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

1) entrada do dado da velocidade que o carro está
2) fazer uma condicional que verifica a velocidade inserida com a velocidade maxima permitida
3) fazer o calculo da multa para cada KM acima do limite que o motorista estiver

'''

velocidadeCarro = int(input("Qual a velocidade que o carro estava: "))

limiteMaximo = 80

if velocidadeCarro > limiteMaximo:
    print(f"Você está acima do limite de velocidade permitido de {limiteMaximo}Km/h. Velocidade Capturada: {velocidadeCarro}Km/h.")
    multa = (velocidadeCarro-80)*7
    print(f"Você deverá pagar uma multa de R${multa}.")
else:
    print("Você estavá dentro do limite de velocidade estabelecido! Tenha um bom dia.")