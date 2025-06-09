print("Exercícios - Repetição com while (Pyhton) \n")

print("4) Elaborar um programa que solicite ao usuário vários valores inteiros. Quando o usuário digitar o número 100 o programa deve terminar, mostrando quantos valores foram acima de 80, quantos foram abaixo de 10 e mostrar a média de todos os valores digitados pelo usuário. \n")

lista = []

men80 = []

men10 = []

num = float(input("Digite um número: \n"))

while (num != 100):
    lista.append(num)

    if num > 80:
        men80.append(num)

    if num < 10:
        men10.append(num)

    num = float(input("Digite outro número, digite 100 se quiser parar. \n"))

else:
    num80 = len(men80)
    num10 = len(men10)

    total = len(lista)
    soma = sum(lista)
    media = soma / total

    print("O total de números menores que 10 no programa foi de %d. O total de números maiores que 80 foi de %d. E a média de todos os números digitados foi de %d" %(num10, num80, media))