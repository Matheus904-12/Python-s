#13)Desenhe um algoritmo que recebe a idade de uma pessoa e informe se possui direito a desconto.
#Regra para obter o desconto é necessário ter menos de 16 anos ou ser idoso (ter a partir de 60 anos).

import os
os .system("cls")

Idade = int(input("Idade: "))

if Idade < 16 or Idade >= 60:
    print("Tem desconto")
else:
    print("Sem desconto")