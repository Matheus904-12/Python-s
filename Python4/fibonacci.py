import os
os .system("cls")
print('Sequência de Fibonacci')

x = 0
anterior = 1
atual = 1
lista = []
lista.append(anterior)

limite = int(input('Digite o elemento desejado\n'))

while (x < limite - 5):
    futuro = anterior + atual
    anterior = atual 
    atual = futuro
    print(futuro)
    lista.append(futuro)
    x += 1
print(sorted(lista, key=int, reverse=True))