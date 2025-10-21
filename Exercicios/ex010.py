# faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input("Qual o preço do produto: "))

desconto = preco * (5/100)

precofinal = preco - desconto

print (f"O produto que custava {preco} com 5% de desconto passa a custar {precofinal}")