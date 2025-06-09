#4) Elaborar um programa que leia o saldo de uma aplicação e imprimir o novo saldo, considerando um reajuste de 15%.
import os
os .system("cls")
saldo = int(input("Coloque o valor do seu saldo: "))
reajuste = saldo * 0.15
NovoSaldo = reajuste + saldo
print("O seu saldo atual é de:", NovoSaldo)