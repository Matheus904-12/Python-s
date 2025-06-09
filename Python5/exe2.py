#Elaborar uma função (com retorno) que verifica se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 0 se for igual a 0.

import os
os .system("cls")

num1 = float(input("Digite um Número: \n"))

def posn(num1):
    
    if num1 > 1:
        print("1 = Positivo")
    elif num1 < 0:
        print("-1 = Negativo")
    else:
        print("0 = Neutro")
    return num1

resultado = posn(num1)
print(f"O número é: {resultado}")