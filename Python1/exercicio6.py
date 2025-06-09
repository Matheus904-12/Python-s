#6) Elaborar um programa que receba a largura e a altura de um retângulo, calcula e mostra sua área e seu perímetro.
import os
os .system("cls")
largura = (input("Digite a largura do retângulo: "))
altura = (input("Digite a altura do retângulo: "))
area = largura * altura
perimetro = 2 * (largura + altura)
print("A área do retângulo é:", area)
print("O perímetro do retângulo é:", perimetro)