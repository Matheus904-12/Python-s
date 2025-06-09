#9)Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é: 2, 3 e 5, respectivamente

import os
os .system("cls")
print("Média Final")
a=int(input("Digite a Primeira Nota:"))
b=int(input("Digite a Segunda Nota:"))
c=int(input("Digite a Terceira Nota:"))
d=a+b+c // 3
print("Média Final é igual a:", d)
