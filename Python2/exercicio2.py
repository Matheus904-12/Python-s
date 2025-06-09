#2) Pedro comprou um saco de ração com peso em quilos. Pedro possui dois gatos para os quais fornece a
#quantidade de ração em gramas. Faça um algoritmo que receba o peso do saco de ração e a quantidade de ração fornecida para cada gato por dia. Calcule e mostre quanto restará de ração no saco após cinco dias.;

import os
os .system("cls")
print("Balança de Ração")

Saco=float(input("Insira o Peso do Saco: "))
Gato1=float(input("Quantidadede Ração por dia para o Gato1: "))
Gato2=float(input("Quantidadede Ração por dia para o Gato2: "))

RacaoGramas = Saco * 1000
Racao_Gatos = Gato1 + Gato2
Racao_Dias = Racao_Gatos * 5
Resto = RacaoGramas - Racao_Dias

print("Peso inicial do saco:", RacaoGramas, "gramas.")
print("Consumo total dos gatos por dia:", Racao_Gatos, "gramas.")
print("Consumo total previsto para 5 dias:", Racao_Dias, "gramas.")
print("Quantidade de ração restante após 5 dias:", Resto, "gramas.")
