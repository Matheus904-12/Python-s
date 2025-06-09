#4) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
#diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de
#pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa
#que você faça um Fluxograma que leia a variável P (peso de peixes) e verifique se há excesso. Se houver,
#gravar na variável E (Excesso) e na variável M o valor da multa que João deverá pagar. Caso contrário
#mostrar tais variáveis com o conteúdo ZERO.

import os
os .system("cls")
print("Pesagem dos Peixes")

Peso_de_Peixes = float(input("Insira o peso do peixes: "))

Peso_Max = 50.0
MultaPKg = 4.00
Excesso = 0.0
Multa = 0.0

if Peso_de_Peixes > Peso_Max:
  Excesso = Peso_de_Peixes - Peso_Max
  Multa = Excesso * MultaPKg

print("Excesso de peso:", Excesso, "kg")
print("Multa a pagar: R$", Multa)