N = int(input("Digite um número maior que 2: \n"))
X = 0
start = 1

while (N <= 2):
    N = int(input("Digite outro número maior que 2: \n"))
    
while (X < N):
    new = X + 1
    quadrado = new * new
    cubo = new * new * new
    print(f"O quadrado de {new} é {quadrado}, o seu cubo é {cubo}")
    X = X + 1

else:
    print("\nFim.")