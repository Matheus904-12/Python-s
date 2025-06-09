lista = []

num = float(input("Digite um número: \n"))

while (num != 0):
    lista.append(num)
    num = float(input("Digite outro número: \n"))

else:
    soma = sum(lista)
    total = len(lista)
    media = soma / total

    print("A somatória das listas é de %0.2f, e sua média é %0.2f" % (soma, media))