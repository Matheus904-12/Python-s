#7) Elaborar um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: 
#- A idade desta pessoa hoje;
#- A idade desta pessoa em 2035
import os
os .system("cls")
Nascimento = int(input("Qual foi o ano que você nasceu? "))
AnoAtual = int(input("Em qual ano estamos? "))
Idade = AnoAtual - Nascimento
IdadeFuturo = 2035 - Nascimento
print("Sua idade é:", Idade)
print("Em 2035 você terá:", IdadeFuturo)