import os
os.system("cls")

N = int(input("Digite um número maior que 2: \n"))

def primo(num1):
    if num1 % 2 == 0 or num1 % 3 == 0 or num1 % 5 == 0:
        return 0
    else:
        return 1

def imprimir_primos(N):
    lista_primos = []
    for numero in range(2, N + 1):
        if primo(numero) == 1:
            lista_primos.append(numero)
    print(f"{lista_primos}")

while (N <= 2):
    N = int(input("Número incorreto, por favor coloque um número maior que 2: \n"))

imprimir_primos(N)