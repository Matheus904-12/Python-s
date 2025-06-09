#3) Elaborar um programa que calcule o consumo médio de um automóvel (medido em km/l), dado que são conhecidos a distância total percorrida e o volume de combustível consumido para percorrê-la (medido em litros)
import os
os .system("cls")
kmPercorrido = int(input("Coloque o Km Percorrido: "))
combustivelGasto = int(input("Coloque o Combustivel Gasto: "))
mediaKml = kmPercorrido / combustivelGasto
print("O consumo médio foi de km/l é:", mediaKml)