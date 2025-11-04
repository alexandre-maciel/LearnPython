'''
4. Conversor de Idade para Meses
Objetivo: Praticar operações aritméticas e formatação de saída.

Instruções:

Peça ao usuário que digite sua idade em anos (número inteiro).

Calcule a idade aproximada em meses (multiplique a idade por 12).

Imprima a idade em anos e a idade calculada em meses em uma única linha, formatada de forma clara.
'''

#declaro uma variavel para receber a idade do usuário
idade = int(input("Qual a sua idade? "))

# faço a conta da idade multiplicada por 12 para encontrar os meses
idade_meses = idade * 12

# chamo um print para mostrar para o usuário a conversão da idade de anos para meses
print(f"A idade de {idade}, equivale a {idade_meses} meses")