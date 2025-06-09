#12)Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro quadrado, deve-se usar 18W de potência. Faça um algoritmo que receba as duas dimensões de um cômodo (em metros). Calcule e mostre a sua área (em m2) e a potência de iluminação que deverá ser utilizada.

import os
os.system("cls")
largura = int(input("Digite a largura do cômodo em metros: "))
comprimento = int(input("Digite o comprimento do cômodo em metros: "))
area = largura * comprimento
potenciaMQ = 18
potenciaT = area * potenciaMQ
print(f"A área do cômodo é:", area, "m²")
print(f"A potência de iluminação necessária é:", potenciaT, "W")