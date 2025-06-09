import os
os .system("cls")

palavra = input("Digite uma palavra ou frase: ")

def palindromo(texto):
    texto = texto.lower().replace("","")
    texto_invertido = texto[::-1]
    return texto == texto_invertido

if palindromo(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")