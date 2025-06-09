#3) Criar um algoritmo que leia a idade de uma pessoa e informar a sua classe eleitoral:
#a. Não-eleitor (abaixo de 16 anos)
#b. Eleitor obrigatório (entre 18 e 65 anos)
#c. Eleitor facultativo (entre 16 e 18 e maior de 65 anos)

import os
os .system("cls")
print("Leitor de Idades")

Idade = int(input("Insira sua Idade: "))

if Idade < 16:
    print("Não Eleitor")
elif Idade >= 18 and Idade <= 65:
    print("Voto Obrigatório")
else:
    print("Opcional")