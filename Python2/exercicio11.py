#11)Desenhe um algoritmo que recebe quatro Números reais e informe se há algum repetido ou não.

import os
os .system("cls")

N1 = float(input("Número 1: "))
N2 = float(input("Número 2: "))
N3 = float(input("Número 3: "))
N4 = float(input("Número 4: "))

if N1 == N2 or N1 == N3 or N1 == N4 or N2 == N3 or N2 == N4 or N3 == N4:
    print("Repetido")
else:
    print("Sem repetição")
