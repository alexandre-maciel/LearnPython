# Peça a nota de um aluno (0-10) e informe se ele foi aprovado (nota ≥ 6).

nome = str(input("Nome do aluno: "))
n1 = float(input("Qual foi a nota da primeira prova: "))
n2 = float(input("Qual a nota do trabalho em grupo: "))

media = (n1 + n2) / 2

if media >= 6:
  print(f"\nO(a) aluno(a) {nome} está aprovado(a)")
else:
  print(f"\nO(a) aluno(a) {nome} está reprovado(a)")