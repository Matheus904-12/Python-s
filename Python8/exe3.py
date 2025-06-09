import os
os .system ("cls")

def inverter_string(texto):
    return texto[::1] #reversed ::-1 vai começar a partir dele mas o -1 ira inverter a ordem da palavra

palavra = input("Digite uma palavra ou número: ")
palavra_invertida = inverter_string(palavra)
print(f"O texto invertido é: {palavra_invertida}")