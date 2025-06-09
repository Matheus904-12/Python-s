num = float(input("Digite um número entre 10 e 15, por favor:\n"))

while (num < 10 or num > 15):
    num = float(input("Entrada inválida, por favor digite outro número:\n"))

else:
    raiz = num ** 0.5
    print("a raíz quadrada do número é %0.2f" %(raiz))