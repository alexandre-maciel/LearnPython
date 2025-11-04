#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

largura = int (input("Qual a largura em metros: "))
altura = int (input ("Qual a altura em metros: "))

area = largura * altura
pintar = area // 2

print (f"A área a ser pintada equivale a {area}m² e necessitam {pintar} litros de tinta para pintar")