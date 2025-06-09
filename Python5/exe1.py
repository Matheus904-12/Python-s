#Elaborar uma função (com retorno) que recebe como parâmetro um número inteiro e devolve o seu dobro.

import os
os .system("cls")

numero = int(input("Digite um número: \n"))

def dobro(numero):
    return numero * 2 

resultado = dobro(numero)
print(f"o dobro de {numero} é: {resultado}")