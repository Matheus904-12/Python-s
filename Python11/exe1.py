

#numeros = []

#for x in range(101):
#   numeros.append(f"{x};")

#numeros.pop(0)


#print(numeros)
import os
os .system("cls")

lista = []
arquivo = open("crescente.txt", "w")
for i in range(100):
    lista.append(i+1)
    if i < 99:
        arquivo.write(str(i+1) + ";")
    else:
        arquivo.write(str(i+1) + ".")
print(lista)
arquivo.close()