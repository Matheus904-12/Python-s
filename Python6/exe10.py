import os
os .system("cls")

lista_de_numeros = []
contador = 0
 
while contador < 15:
    try:
        entrada = input(f"Digite o {contador + 1}º número inteiro: ")
        numero = int(entrada)
 
        # Verificar se o número já está na lista
        numero_ja_existe = False
        indice = 0
        while indice < len(lista_de_numeros):
            if lista_de_numeros[indice] == numero:
                numero_ja_existe = True
                break
            indice = indice + 1
 
        if not numero_ja_existe:
            lista_de_numeros.append(numero)
            contador = contador + 1
        else:
            print("Esse número já foi digitado. Por favor, digite um número diferente.")
 
    except ValueError:
        print("Você digitou algo que não é um número inteiro. Tente novamente.")
 
print("\nLista final de números únicos:")
indice_final = 0
while indice_final < len(lista_de_numeros):
    print(lista_de_numeros[indice_final])
    indice_final = indice_final + 1