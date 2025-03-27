# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metro = int(input("insira o valor em metros "))

cm = metro*100
mm = metro*1000

print(f"A medida em centimetros é {cm}")
print(f"A medida em milimetros é {mm}")