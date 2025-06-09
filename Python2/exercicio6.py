#6) Elabore um algoritmo que lê um número inteiro entre 1 e 7 e exibe o dia da semana correspondente. Caso o
#usuário digite um número fora desse intervalo, o algoritmo mostra uma mensagem informando “Número
#inválido”.

import os
os .system("cls")
print("Intervalos da Semana")

Num = int(input("Digite um número inteiro entre 1 e 7: "))

if Num < 1 or Num > 7:
    print("Numero_Invalido")
else:
    if Num == 1:
        print("Segunda")
    elif Num == 2:
        print("Terca")
    elif Num == 3:
        print("Quarta")
    elif Num == 4:
        print("Quinta")
    elif Num == 5:
        print("Sexta")
    elif Num == 6:
        print("Sabado")
    else:
        print("Domingo")