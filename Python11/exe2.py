import os
os .system("cls")

x = 100

lista = []
arquivo = open("crescente2.txt", "w")
#for i in range(100):
x = 100
while x > 0:
    lista.append(x)
    if x > 1:
        arquivo.write(str(x) + ";")
    else:
        arquivo.write(str(x) + ".")
    x = x - 1
print(lista)
arquivo.close()
