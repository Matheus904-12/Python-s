#5) Mária recebeu seu salário e precisa pagar duas contas que estão
#atrasadas. Como as contas estão atrasadas, Mária terá que pagar multa de
#2% sobre cada conta. Faça um algoritmo que calcule e mostre quanto
#restará do salário de Mária.

import os
os .system("cls")
print("Pagar Contas")

Salario = float(input("Digite seu salario: "))
Conta1 = float(input("Preço da Conta1: "))
Conta2 = float(input("Preço da Conta2: "))

Atrasada1 = Conta1 + (Conta1 / 50)
Atrasada2 = Conta2 + (Conta2 / 50)
Despesa = Atrasada1 + Atrasada2
Sobra = Salario - Despesa

print("A multa da Conta1 deu: R$", Atrasada1)
print("A multa da Conta2 deu: R$", Atrasada2)
print("Totalizando:", Despesa, "em despesas")
print("Sobrou: R$", Sobra)

