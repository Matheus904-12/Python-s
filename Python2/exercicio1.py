#1) Criar um algoritmo receba a média de um aluno e mostre a situação do aluno:
#a. Aprovado à média maior ou igual a 5;
#b. Exame à média entre 3 e 5;
#c. Reprovado à média menor do que 3;

import os
os .system("cls")
print("Média de um Aluno")

nota1 = float(input("Insira Sua Primeira Nota: "))
nota2 = float(input("Insira Sua Segunda Nota: "))
nota3 = float(input("Insira Sua Terceira Nota: "))

MF = (nota1 + nota2 + nota3) / 3
print(f"\nA Média Final do aluno é: {MF:.2f}")

print("Situação do Aluno:")
if MF >= 5:
    print("Aprovado")
elif MF >= 3:
    print("Exame")
else:
    print("Reprovado")