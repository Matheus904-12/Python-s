#10)Faça um algoritmo que receba o custo de um espetáculo teatral e o preço do convite deste espetáculo. Esse algoritmo deve calcular e mostrar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.

import os
os .system("cls")
print("Espetáculo Teatral")
espetaculoTeatral = int(input("Coloque o Custo do Espetáculo Teatral: "))
precoConvite = int(input("Coloque o Preço do Convite: "))
custoTotal = espetaculoTeatral // precoConvite 
print("O Custo Total do Espetáculo é:", custoTotal)