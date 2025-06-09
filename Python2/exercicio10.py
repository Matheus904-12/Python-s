#10)Desenhe o fluxograma e implemente um programa que leia dois números inteiros e informe qual é o maior.

import os
os .system("cls")

N1 = float(input("Primeiro número: "))
N2 = float(input("Segundo número: "))

if N1 > N2:
    print(f"{N1} é maior")
elif N2 > N1:
    print(f"{N2} é maior")
else:
    print("São iguais")