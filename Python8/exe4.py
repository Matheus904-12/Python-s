import os
os .system ("cls")

vogal= []

consol = []

y = 0

palavra = input("Digite uma palavra: \n")

tamanho = len(palavra)

for n in range(tamanho):
    ponteiro = palavra[y]

    if ponteiro == "a" or ponteiro == "A" or ponteiro == "E" or ponteiro == "e" or ponteiro == "I" or ponteiro == "i" or ponteiro == "O" or ponteiro == "o" or ponteiro == "U" or ponteiro == "u":
        vogal.append(ponteiro)
    else:
        consol.append(ponteiro)

    y = y + 1

print(f"{consol}")