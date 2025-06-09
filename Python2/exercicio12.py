#12)Desenhe um algoritmo que recebe três números inteiros e informe se são números consecutivos em ordem crescente.

import os
os .system("cls")

N1 = int(input("Número 1: "))
N2 = int(input("Número 2: "))
N3 = int(input("Número 3: "))

if N2 == N1 + 1 and N3 == N2 + 1:
    print("Consecutivos")
else:
    print("Não consecutivos")
