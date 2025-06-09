#11)Faça um algoritmo (Fluxograma) que receba o peso de uma pessoa em quilos. Calcule e mostre:
#a. O novo peso se a pessoa engordar 15% sobre o peso digitado;
#b. O novo peso se a pessoa emagrecer 20% sobre o peso digitado;

import os
os .system("cls")
Peso = int(input("Insira seu Peso: "))
aumento_percentual = 0.15
novo_peso_engordar = Peso + (Peso * aumento_percentual)
diminuicao_percentual = 0.20
novo_peso_emagrecer = Peso - (Peso * diminuicao_percentual)
print("O novo peso se a pessoa engordar 15% é:", novo_peso_engordar, "kg")
print("O novo peso se a pessoa emagrecer 20% é:", novo_peso_emagrecer, "kg")