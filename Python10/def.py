import os
os .system("cls")

busca_usuario = input("Digite o nome do produto do estoque: ")

def buscar_produto(lista_produtos, termo_busca):
    termo_busca_lower = termo_busca.lower()
    resultados = []
    for produto in lista_produtos: #termos da lista de produtos
        produto_lower = produto.lower()
        if termo_busca_lower in produto_lower: #termo do usuario
            resultados.append(produto)
    return resultados
    
produtos_ecommerce = [
        "Computador",
        "Teclado",
        "Mouse",
        "Monitor",
        "Cadeira",
        "Mesa",
        "WebCam",
        "Câmera"
    ]

produtos_encontrados = buscar_produto(produtos_ecommerce, busca_usuario)

if produtos_encontrados:
    print("Produtos encontrados:")
    for produto in produtos_encontrados:
        print(f"-{produto}")
else:
    print("Nenhum produto encontrado!")