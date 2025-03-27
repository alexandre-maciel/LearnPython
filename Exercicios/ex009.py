#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

larg = int(input("insira a largura da parede "))
alt = int(input("insira a altura da parede "))

area = larg*alt
pintar = area//2

print(f"area é de {area}m²")
print(f"A quantidade necessaria para pintar a parede é de {pintar}L de tinta")