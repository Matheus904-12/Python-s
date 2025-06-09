#6) Elaborar uma função (sem retorno) que recebe dois valores inteiros passados como parâmetro. Logo em seguida a função deve exibir um menu com 4 opções (cada opção levará para uma função com retorno diferente):

import math

resultado = None

def somar(a, b):
    global resultado
    resultado = a + b

def subtrair(a, b):
    global resultado
    resultado = a - b

def multiplicar(a, b):
    global resultado
    resultado = a * b

def dividir(a, b):
    global resultado
    if b != 0:
        resultado = a / b
    else:
        resultado = "Erro: Divisão por zero!"

def calcular_raiz_quadrada(num):
    global resultado
    resultado = math.sqrt(num)

def exibir_menu_e_calcular(num1, num2):
    global resultado
    continuar = True
    while continuar:
        print("\nEscolha uma operação:")
        print("a) Soma")
        print("b) Subtrair")
        print("c) Multiplicar")
        print("d) Dividir")
        print("e) Raiz quadrada do primeiro número")
        print("f) Sair")

        opcao = input("Digite a letra da operação desejada: ")

        if opcao == 'a':
            somar(num1, num2)
            print(f"Resultado da Soma: {resultado}")
        elif opcao == 'b':
            subtrair(num1, num2)
            print(f"Resultado da Subtração: {resultado}")
        elif opcao == 'c':
            multiplicar(num1, num2)
            print(f"Resultado da Multiplicação: {resultado}")
        elif opcao == 'd':
            dividir(num1, num2)
            print(f"Resultado da Divisão: {resultado}")
        elif opcao == 'e':
            calcular_raiz_quadrada(num1)
            print(f"Raiz quadrada: {resultado}")
        elif opcao == 'f':
            print("Saindo...")
            continuar = False
        else:
            print("Opção inválida. Tente novamente.")

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

exibir_menu_e_calcular(numero1, numero2)