#9) Desenhe um algoritmo que recebe dois números inteiros e mostre o resultado da divisão deles. Se o segundo número é igual a zero, informe que é impossível devido à divisão por zero.

import os
os .system("cls")

Num1 = int(input("Primeiro número: "))
Num2 = int(input("Segundo número: "))

if Num2 == 0:
    print("Erro: Divisão por zero!")
else:
    print(f"Resultado: {Num1 / Num2}")