#2) Elaborar um programa que receba quatro números inteiros, que calcule e mostre a soma e a média desses números.
import os
os .system("cls")
n1 = int(input("Coloque o Primeiro Número: "))
n2 = int(input("Coloque o Segundo Número: "))
n3 = int(input("Coloque o Terceiro Número: "))
n4 = int(input("Coloque o Quarto Número: "))
soma = n1 + n2 + n3 + n4
media = soma/4
print("A soma dos numeros é de:", soma)
print("A Média é de:", media)