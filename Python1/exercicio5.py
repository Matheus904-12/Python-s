#5) Elaborar um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário
import os
os .system("cls")
Salario = int(input("Qual é o seu salário atual? "))
Percentual = int(input("Qual foi o percentual de aumento? "))
Percentual2 = Percentual / 100
Aumento = Salario * Percentual2
NovoSalario = Aumento + Salario
print("Seu salário teve um aumentou de R$", Aumento)
print("Seu salário atual é R$", NovoSalario)