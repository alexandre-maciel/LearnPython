'''

Faça um programa que leia três números e mostre qual é o maior e qual é o menor

1) entrada dos 3 numeros
2) condicional com elif para descobrir o numero maior

'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"O número {n1} é o maior")
elif n2 > n1 and n2 > n3:
    print(f"O número {n2} é o maior")
else: 
    print(f"O número {n3} é o maior")
