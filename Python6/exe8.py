lista = []

num = int(input("Digite um número positivo/par para adicionar à lista: \n"))
while (num != 1):
    if (num % 2 == 0 and num > 0):
        lista.append(num)
        num = int(input("Digite outro número para adicionar á lista, (digite 1 para finalizar a requisição): \n"))
    else:
        num = int(input("Número não se encaixa nos parâmetros acima, não computado na lista. Adicione outro número: \n"))
else:
    print(lista)
    print('Fim do programa')
    