import os
os .system("cls")
print('Atividade 3')

num = int(input("Digite um número: "))

if num <= 0:
    print('Número Inválido, digite um número inteiro maior que 0')
elif num == 1:
    print("Valor inválido, 1 não é considerado número primo")
elif num == 2 or num == 3 or num == 5 or num == 7:
    print('Número primo')
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print('O número não é primo')
else:
    print('Número primo')
