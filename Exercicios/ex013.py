# escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

# entrada da quantidade de km rodados pelo carro alugado
# quantidade de dias pelos quais ele foi alugado
# calcular o preço pelos dias alugados com a diaria a 60 reais 
# calcular os km rodados sendo 0,15 centavos por km rodado
# calcular a soma dos dois e mostrar o resultado

km_rodado = float(input("Quantos quilometros o carro percorreu: "))
dias_alugados = int(input("Quantos dias foram alugados: "))

preco_dia = dias_alugados * 60
preco_km = km_rodado * 0.15

preco_total = preco_dia + preco_km

print (f"O preço total pelo aluguel do carro foi igual a R${preco_total:.2f}")



# kmrodado = int(input("Quantos kilometros rodados: "))
# dias = int(input("Quantos dias alugados: "))

# precoKm = kmrodado * 0.15
# precoDia = dias * 60

# print(f"o preço total dos Km rodado do carro foi de R${precoKm:.2f}")
# print(f"o preço total dos dias alugados do carro foi de R${precoDia:.2f}")


# totalPreco = precoKm + precoDia

# print(f"o preço total do aluguel do carro foi de R${totalPreco:.2f}")