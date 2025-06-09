import os
os.system("cls")

print("Sistema de Cadastro de Produtos")

# Variáveis globais
confirm = "s"
confirmar = "s"
produto_id = 100  # Código inicial dos produtos
produtos = {}  # Dicionário para armazenar produtos: {id: [desc, preco]}
operador_produtos = {}  # Dicionário para produtos associados ao operador: {id: [desc, preco]}

# Funções

def menu():  # Menu principal
    print("\n1) Administrador")
    print("2) Operador")
    print("3) Sair")
    option = str(input("Digite qual opção deseja (escreva um número de 1 a 3): ")).strip()
    while option not in ["1", "2", "3"]:
        option = str(input("Por favor, digite um número correto (de 1 a 3): ")).strip()
    return option

def menuADM():  # Menu do administrador
    print("\n1) Cadastrar produto")
    print("2) Listar produtos")
    print("3) Editar produto")
    print("4) Excluir produto")
    print("5) Voltar")
    optionadm = str(input("Digite qual opção deseja (escreva um número de 1 a 5): ")).strip()
    while optionadm not in ["1", "2", "3", "4", "5"]:
        optionadm = str(input("Por favor, digite um número correto (de 1 a 5): ")).strip()
    return optionadm

def menuOperador():  # Menu do operador
    print("\n1) Adicionar produto à conta")
    print("2) Listar meus produtos")
    print("3) Voltar")
    optionop = str(input("Digite qual opção deseja (escreva um número de 1 a 3): ")).strip()
    while optionop not in ["1", "2", "3"]:
        optionop = str(input("Por favor, digite um número correto (de 1 a 3): ")).strip()
    return optionop

def cadastrar_produto():  # Função para administrador cadastrar produtos
    global produto_id
    desc = str(input("Digite a descrição do produto: ")).strip()
    while not desc:
        desc = str(input("Descrição não pode ser vazia. Digite novamente: ")).strip()
    
    try:
        preco = float(input("Digite o preço do produto: "))
        while preco <= 0:
            preco = float(input("Preço deve ser maior que zero. Digite novamente: "))
    except ValueError:
        print("Preço inválido. Operação cancelada.")
        return
    
    produtos[produto_id] = [desc, preco]
    print(f"Produto cadastrado com sucesso! Código: {produto_id}")
    produto_id += 1  # Incrementa o código para o próximo produto
    salvar_arquivo()

def listar_produtos():  # Função para listar todos os produtos (administrador)
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for codigo, info in produtos.items():
            print(f"[Código: {codigo}, Descrição: {info[0]}, Preço: {info[1]}]")

def editar_produto():  # Função para administrador editar produtos
    listar_produtos()
    if not produtos:
        return
    
    try:
        codigo = int(input("Digite o código do produto a editar: "))
        if codigo not in produtos:
            print("Produto não encontrado.")
            return
        
        desc = str(input("Digite a nova descrição do produto (ou pressione Enter para manter): ")).strip()
        if desc:
            produtos[codigo][0] = desc
        
        preco_input = str(input("Digite o novo preço do produto (ou pressione Enter para manter): ")).strip()
        if preco_input:
            try:
                preco = float(preco_input)
                if preco <= 0:
                    print("Preço deve ser maior que zero. Operação cancelada.")
                    return
                produtos[codigo][1] = preco
            except ValueError:
                print("Preço inválido. Operação cancelada.")
                return
        
        print("Produto editado com sucesso!")
        salvar_arquivo()
    except ValueError:
        print("Código inválido.")

def excluir_produto():  # Função para administrador excluir produtos
    listar_produtos()
    if not produtos:
        return
    
    try:
        codigo = int(input("Digite o código do produto a excluir: "))
        if codigo not in produtos:
            print("Produto não encontrado.")
            return
        
        sure = str(input("Você tem certeza que deseja excluir o produto? (s/n): ")).strip().lower()
        if sure == "s":
            del produtos[codigo]
            if codigo in operador_produtos:
                del operador_produtos[codigo]  # Remove também da lista do operador
            print("Produto excluído com sucesso!")
            salvar_arquivo()
        else:
            print("Operação cancelada.")
    except ValueError:
        print("Código inválido.")

def adicionar_produto_operador():  # Função para operador adicionar produtos à sua conta
    listar_produtos()
    if not produtos:
        return
    
    try:
        codigo = int(input("Digite o código do produto a adicionar à sua conta: "))
        if codigo not in produtos:
            print("Produto não encontrado.")
            return
        
        operador_produtos[codigo] = produtos[codigo]
        print("Produto adicionado à sua conta com sucesso!")
        salvar_arquivo_operador()
    except ValueError:
        print("Código inválido.")

def listar_produtos_operador():  # Função para operador listar seus produtos
    if not operador_produtos:
        print("Nenhum produto associado à sua conta.")
    else:
        print("\nSeus Produtos:")
        for codigo, info in operador_produtos.items():
            print(f"[Código: {codigo}, Descrição: {info[0]}, Preço: {info[1]}]")

def salvar_arquivo():  # Salva produtos no arquivo
    with open("exe3/cadastro_produtos.txt", "w") as arquivo:
        for codigo, info in produtos.items():
            arquivo.write(f"codigo:{codigo} desc:{info[0]} preco:{info[1]}\n")

def salvar_arquivo_operador():  # Salva produtos do operador no arquivo
    with open("exe3/cadastro_operador.txt", "w") as arquivo:
        for codigo, info in operador_produtos.items():
            arquivo.write(f"codigo:{codigo} desc:{info[0]} preco:{info[1]}\n")

def carregar_arquivos():  # Carrega produtos dos arquivos ao iniciar
    global produto_id
    try:
        with open("exe3/cadastro_produtos.txt", "r") as arquivo:
            for linha in arquivo:
                try:
                    parts = linha.strip().split()
                    codigo = int(parts[0].split(":")[1])
                    desc = parts[1].split(":")[1]
                    preco = float(parts[2].split(":")[1])
                    produtos[codigo] = [desc, preco]
                    if codigo >= produto_id:
                        produto_id = codigo + 1
                except (IndexError, ValueError):
                    continue
    except FileNotFoundError:
        pass  # Arquivo não existe ainda, será criado ao salvar

    try:
        with open("exe3/cadastro_operador.txt", "r") as arquivo:
            for linha in arquivo:
                try:
                    parts = linha.strip().split()
                    codigo = int(parts[0].split(":")[1])
                    desc = parts[1].split(":")[1]
                    preco = float(parts[2].split(":")[1])
                    operador_produtos[codigo] = [desc, preco]
                except (IndexError, ValueError):
                    continue
    except FileNotFoundError:
        pass

# Main
carregar_arquivos()  # Carrega dados dos arquivos ao iniciar

while confirm == "s":
    escolha = menu()

    if escolha == "1":  # Administrador
        while confirmar == "s":
            escolhaADM = menuADM()
            if escolhaADM == "1":
                cadastrar_produto()
            elif escolhaADM == "2":
                listar_produtos()
            elif escolhaADM == "3":
                editar_produto()
            elif escolhaADM == "4":
                excluir_produto()
            elif escolhaADM == "5":
                confirmar = "n"
            else:
                print("[ERRO] Dígito inválido")
            input("Pressione Enter para continuar...")

    elif escolha == "2":  # Operador
        confirmar = "s"
        while confirmar == "s":
            escolhaOP = menuOperador()
            if escolhaOP == "1":
                adicionar_produto_operador()
            elif escolhaOP == "2":
                listar_produtos_operador()
            elif escolhaOP == "3":
                confirmar = "n"
            else:
                print("[ERRO] Dígito inválido")
            input("Pressione Enter para continuar...")

    elif escolha == "3":
        print("Fim da execução")
        confirm = "n"
    else:
        print("[ERRO] Dígito inválido")
    input("Pressione Enter para continuar...")
    os.system("cls")