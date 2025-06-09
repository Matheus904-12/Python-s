import os
os .system("cls")
print('Atividade 2')

lado1 = float(input("Escreva o lado 1 do triângulo: "))
lado2 = float(input("Escreva o lado 2 do triângulo: "))
lado3 = float(input("Escreva o lado 3 do triângulo: "))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
	print("Triângulo Inválido")
elif lado1 == lado2 and lado1 == lado3:
	print("Triângulo Equilatero")
elif lado1 == lado2 or lado1 == lado3:
	print("Triângulo Isóceles")
else:
	print("Triângulo Escaleno")