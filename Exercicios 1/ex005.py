# desenvolva um programa que leia duas notas de um aluno, calcule sua media

nota1 = int (input("Qual foi a primeira nota: "))
nota2 = int (input("Qual foi a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Você foi aprovado!")
else:
    print ("Você está de recuperação!")
