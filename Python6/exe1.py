cel = float(input("Digite a temperatura em Celsius: \n"))

while (cel > -5 ):
    F = ( cel * 1.8 ) + 32
    K = cel + 273
    print(f"A temperatura {cel} em Fahrenheint é {F} e em Kelvin é {K}.")
    cel = float(input("Digite outra: \n"))

print("Fim.")