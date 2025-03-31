# Peça 3 números e exiba o maior.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3= int(input("Terceiro número: "))

if n1>=n2 and n1>=n3:
  print(f"O número {n1} é maior que {n2} e {n3}")
elif n2>=n1 and n2>=n3:
  print(f"o {n2} é maior número que {n1} e {n3}")
else:
  print(f"o {n3} é o maior que {n1} e {n2}")
