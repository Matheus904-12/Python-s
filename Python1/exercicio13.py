#13)Faça um algoritmo que receba o número de horas trabalhadas e o valor do salário mínimo. Calcule e mostre o salário a receber seguindo as regras abaixo:
#a. o valor da hora trabalhada vale a metade do salário mínimo;
#b. o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalhada;
#c. o imposto equivale a 3% do salário bruto;
#d. o salário a receber equivale ao salário bruto menos o imposto.

import os
os .system("cls")
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
salario_minimo = int(input("Digite o valor do salário mínimo: "))
valorH = salario_minimo / 2
salario_bruto = horas_trabalhadas * valorH
imposto_percentual = 0.03
imposto = salario_bruto * imposto_percentual
salario_receber = salario_bruto - imposto
print("O valor da hora trabalhada é: R$", valorH)
print("O salário bruto é: R$", salario_bruto)
print("O valor do imposto é: R$", imposto)
print("O salário a receber é: R$", salario_receber)