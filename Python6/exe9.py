print("Exercícios - Repetição com while (Pyhton)\n")

print("9)Elaborar um programa que contenha uma lista com 25 elementos em que o usuário deve preencher com valores reais. Logo em seguida, deve ser solcitado ao usuário que digite dois números. Esses números devem corresponder a posição na lista (caso contrário solicite um novo valor). Após inserir os dois números o programa deve exibir a soma dos elementos das duas posições da lista \n")

lista = []

x = 0

while (x < 25):
    num = float(input("Digite um número:\n"))
    lista.append(num)
    x = x + 1

num1 = int(input("Digite um número inteiro, entre 0 e 24, por favor: \n"))
num2 = int(input("Digite um segundo número inteiro, entre 1 e 24, por favor: \n"))

while (num1 < 0 or num2 < 0 or num1 > 24 or num2 > 24):
    num1 = int(input("Valor errado. Digite um número inteiro, entre 0 e 24, por favor: \n"))
    num2 = int(input("Digite um segundo número inteiro, entre 0 e 24, por favor: \n"))

valor1 = lista[num1]
valor2 = lista[num2]

soma = valor1 + valor2

print("A soma das posições %d e %d são %0.1f " %(num1, num2, soma))