# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = int(input("insira o preço do produto: "))

desconto = preco*(5/100)

precofinal = preco - desconto

print(f"O desconto desse produto em 5% será de R${precofinal} reais")