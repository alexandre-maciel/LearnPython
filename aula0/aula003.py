# modulos

# importando o modulo completo
import math

# importando apenas uma função
from math import sqrt

# agora quando for referenciar só utilizar o sqrt e não math.sqrt

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)

print(f"A raiz de {num} é igual a {math.ceil(raiz)}")