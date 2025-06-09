#Elaborar uma função (com retorno) que ao receber um número deve converte em Kelvin e exibe o resultado na tela. A fórmula de conversão é: K=C+273.15.

#Elaborar uma função (sem retorno) que ao receber um número deve converte em Fahrenheit e exibe o resultado na tela. A fórmula de conversão é: F = (9*C+160) / 5.

import os
os .system("cls")

num1 = float(input("Digite um número: \n"))
def Kel(num1):
    K = num1 + 273.15
    return K

resultado = Kel(num1)

print(f"o número em kelvin é {resultado}")
