import os
os .system ("cls")

print("Exercícios - String")

print("5) Elaborar um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palvra. Depois o usuário deve digitar um caractere (vogal ou consoante) e o programa deve substituir todas as vogais da palvra por esse caractere. \n")

conso = []
vol = []
palavra = []

pal = str(input("Digite uma palavra: \n")) #input

tamanhoPAL = len(pal) #tamanho da palvra

y = 0 #ponteiro

for n in range(tamanhoPAL): #uma repetição para cada letra
    letra = pal[y] #definindo as letras em palavra

    if letra != "a" and letra != "A" and letra != "E" and letra != "e" and letra != "I" and letra != "i" and letra != "O" and letra != "o" and letra != "U" and letra != "u": #conferindo se a letra é uma consoante

        conso.append(letra) #se for consoante, adicione em consol
    else:
        vol.append(letra) #se for vogal, aiciona em vogal

    palavra.append(letra) #sempre será adicionada uma letra para palvra
    y = y + 1
        
tamanhoVol = len(vol) #quantidade de vogais

print(f"{palavra} \n") #print da palavra 

carac = str(input("Digite uma letra: \n")) #perguntando caractere

caprichoV2 = len(carac) 

while caprichoV2 > 1:
    carac = str(input("Digite apenas UMA letra: \n"))
    caprichoV2 = len(carac) #condição caso a palavra tenha mais de 1 caractere

for n in range(tamanhoPAL):
    if palavra[n] == "a":
        palavra[n] = f"{carac}"

    if palavra[n] == "e":
        palavra[n] = f"{carac}"

    if palavra[n] == "i":
        palavra[n] = f"{carac}"

    if palavra[n] == "o":
        palavra[n] = f"{carac}"

    if palavra[n] == "u":
        palavra[n] = f"{carac}"

    if palavra[n] == "A":
        palavra[n] = f"{carac}"

    if palavra[n] == "E":
        palavra[n] = f"{carac}"

    if palavra[n] == "I":
        palavra[n] = f"{carac}"

    if palavra[n] == "O":
        palavra[n] = f"{carac}"

    if palavra[n] == "U":
        palavra[n] = f"{carac}"

print(f"{palavra}")