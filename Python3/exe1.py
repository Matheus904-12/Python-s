import os
os .system("cls")
print('Atividade 1')

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura * altura)

print(f"Seu Indice de Massa Corporal é {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso Normal")
elif imc < 29.9:
    print("Sobepeso")
else:
    print("Obesidade")