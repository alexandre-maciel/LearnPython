# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

kmrodado = int(input("Quantos kilometros rodados: "))
dias = int(input("Quantos dias alugados: "))

precoKm = kmrodado * 0.15
precoDia = dias * 60

print(f"o preço total dos Km rodado do carro foi de R${precoKm:.2f}")
print(f"o preço total dos dias alugados do carro foi de R${precoDia:.2f}")


totalPreco = precoKm + precoDia

print(f"o preço total do aluguel do carro foi de R${totalPreco:.2f}")