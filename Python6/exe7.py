codigo = [100, 101, 102, 103, 104, 105]
produto = ['Cachorro Quente', 'Bauru Simples', 'Bauru c/ovo', 'Hamburguer', 'Chesseburguer', 'Refrigerante']
preco = [3.5, 3.8, 4.5, 4.7, 5.3, 4.0]
total = 0

while True:
    cod = int(input("Digite o código do produto (ou 0 para sair): "))

    if cod == 0:
        break
    if cod in codigo:
        quantidade = int(input(f"Digite a quantidade de {produto[codigo.index(cod)]} que deseja: "))
        while quantidade <= 0:
            print("A quantidade deve ser maior que zero!")
            quantidade = int(input(f"Digite a quantidade de {produto[codigo.index(cod)]} que deseja: "))
        total += preco[codigo.index(cod)] * quantidade
    else:
        print("Código Inválido! Tente Novamente.")

print("\nFim da compra")
print(f"Valor total de compra: R$ {total:.2f}")