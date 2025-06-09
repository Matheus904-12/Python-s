#8) Desenhe um fluxograma e implemente um programa que recebe um número inteiro e informe se é par ou
#ímpar.

import os
os .system("cls")
print("Impar ou Par")

Num = int(input("Digite um número: "))

if Num % 2 == 0:
    print("Par")
else:
    print("Impar")