import os
os.system("cls")

print("Sistema de Cadastro de Produtos")

# Variáveis globais

produto_id = 100  # Código inicial dos produtos
produtos = {}  # Dicionário: {id: [desc, preco, quantidade]}
operador_produtos = {}  # Dicionário: {id: [desc, preco, quantidade_consumida]}

# Funções

def menu(): #Menu Principal
    os.system("cls")
    print("1) Administrador")
    print("2) Operador")
    print("3) Sair")
    return input("Digite a opção (1 a 3): ").strip()

def menuADM(): #Menu do Administrador
    os.system("cls")
    print("\nMenu do Administrador")
    print("1) Cadastrar produto")
    print("2) Listar produtos")
    print("3) Editar produto")
    print("4) Excluir produto")
    print("5) Voltar")
    return input("Digite a opção (1 a 5): ").strip()

def menuOperador(): #Menu do Operador
    os.system("cls")
    print("\nMenu do Operador")
    print("1) Consumir produto")
    print("2) Listar produtos consumidos")
    print("3) Voltar")
    return input("Digite a opção (1 a 3): ").strip()

def cadastrar_produto(): #Cadastro dos Produtos
    os.system("cls")
    global produto_id
    desc = input("Digite a descrição do produto: ").strip()
    while not desc:
        desc = input("Descrição não pode ser vazia. Digite novamente: ").strip()

    preco_input = input("Digite o preço do produto: ")
    if not preco_input.replace('.', '', 1).isdigit():
        print("Entrada inválida. Cadastro cancelado.")
        return
    preco = float(preco_input)
    while preco <= 0:
        preco_input = input("Preço deve ser maior que zero. Digite novamente: ")
        if not preco_input.replace('.', '', 1).isdigit():
            print("Entrada inválida. Cadastro cancelado.")
            return
        preco = float(preco_input)

    quantidade_input = input("Digite a quantidade em estoque: ")
    if not quantidade_input.isdigit():
        print("Entrada inválida. Cadastro cancelado.")
        return
    quantidade = int(quantidade_input)
    while quantidade < 0:
        quantidade_input = input("Quantidade não pode ser negativa. Digite novamente: ")
        if not quantidade_input.isdigit():
            print("Entrada inválida. Cadastro cancelado.")
            return
        quantidade = int(quantidade_input)

    produtos[produto_id] = [desc, preco, quantidade]
    print(f"Produto cadastrado! Código: {produto_id}")
    produto_id += 1
    salvar_arquivo()

def listar_produtos(): #Listagem dos Produtos
    os.system("cls")
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("\nLista de Produtos:")
        for codigo, info in produtos.items():
            print(f"Código: {codigo}, Descrição: {info[0]}, Preço: R${info[1]:.2f}, Estoque: {info[2]}")

def editar_produto(): #Edição dos Produtos
    os.system("cls")
    listar_produtos()
    if not produtos:
        return

    codigo_input = input("Digite o código do produto a editar: ")
    if not codigo_input.isdigit():
        print("Código inválido.")
        return
    codigo = int(codigo_input)
    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    desc = input("Nova descrição (Enter para manter): ").strip()
    if desc:
        produtos[codigo][0] = desc

    preco_input = input("Novo preço (Enter para manter): ").strip()
    if preco_input:
        if not preco_input.replace('.', '', 1).isdigit():
            print("Preço inválido.")
            return
        preco = float(preco_input)
        if preco <= 0:
            print("Preço deve ser maior que zero.")
            return
        produtos[codigo][1] = preco

    quant_input = input("Nova quantidade (Enter para manter): ").strip()
    if quant_input:
        if not quant_input.isdigit():
            print("Quantidade inválida.")
            return
        quantidade = int(quant_input)
        if quantidade < 0:
            print("Quantidade não pode ser negativa.")
            return
        produtos[codigo][2] = quantidade

    print("Produto editado com sucesso!")
    salvar_arquivo()

def excluir_produto(): #Exclusão dos Produtos
    os.system("cls")
    listar_produtos()
    if not produtos:
        return

    codigo_input = input("Digite o código do produto a excluir: ")
    if not codigo_input.isdigit():
        print("Código inválido.")
        return
    codigo = int(codigo_input)
    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    if input("Tem certeza que deseja excluir? (s/n): ").strip().lower() == "s":
        del produtos[codigo]
        if codigo in operador_produtos:
            del operador_produtos[codigo]
        print("Produto excluído!")
        salvar_arquivo()
        salvar_arquivo_operador()
    else:
        print("Operação cancelada.")

def adicionar_produto_operador(): #Salvamento de Produtos do Operador
    os.system("cls")
    listar_produtos()
    if not produtos:
        return

    codigo_input = input("Digite o código do produto a consumir: ")
    if not codigo_input.isdigit():
        print("Código inválido.")
        return
    codigo = int(codigo_input)
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    if produtos[codigo][2] <= 0:
        print("Produto fora de estoque.")
        return

    quantidade_input = input("Digite a quantidade a consumir: ")
    if not quantidade_input.isdigit():
        print("Quantidade inválida.")
        return
    quantidade = int(quantidade_input)
    if quantidade <= 0:
        print("Quantidade deve ser maior que zero.")
        return
    if quantidade > produtos[codigo][2]:
        print(f"Estoque insuficiente. Disponível: {produtos[codigo][2]} unidades.")
        return

    # Atualiza o estoque
    produtos[codigo][2] -= quantidade

    # Registra o consumo do operador
    if codigo in operador_produtos:
        operador_produtos[codigo][2] += quantidade
    else:
        operador_produtos[codigo] = [produtos[codigo][0], produtos[codigo][1], quantidade]

    print(f"{quantidade} unidade(s) do produto '{produtos[codigo][0]}' adicionada(s) à sua conta!")
    salvar_arquivo()
    salvar_arquivo_operador()

def listar_produtos_operador(): #Listagem dos Produtos do Operador
    os.system("cls")
    if not operador_produtos:
        print("Nenhum produto consumido.")
    else:
        print("\nProdutos Consumidos:")
        total = 0
        for codigo, info in operador_produtos.items():
            subtotal = info[1] * info[2]
            print(f"Código: {codigo}, Descrição: {info[0]}, Preço: R${info[1]:.2f}, Quantidade: {info[2]}, Subtotal: R${subtotal:.2f}")
            total += subtotal
        print(f"Total consumido: R${total:.2f}")

#Arquivos TXT

def salvar_arquivo(): #Salvamento dos Cadastros dos Produtos do TXT

    if not os.path.exists("Cadastros"): # Cria a pasta Cadastros se não existir
        os.mkdir("Cadastros")
    
    with open("Cadastros/cadastro_produtos.txt", "w") as arquivo:
        for codigo, info in produtos.items():
            arquivo.write(f"codigo:{codigo} desc:{info[0]} preco:{info[1]} quant:{info[2]}\n")

def salvar_arquivo_operador(): #Salvamento dos Cadastros dos Produtos do Operador no TXT
    
    if not os.path.exists("Cadastros"): #Cria a pasta Cadastros se não existir
        os.mkdir("Cadastros")
        
    with open("Cadastros/cadastro_operador.txt", "w") as arquivo:
        for codigo, info in operador_produtos.items():
            arquivo.write(f"codigo:{codigo} desc:{info[0]} preco:{info[1]} quant:{info[2]}\n")

def carregar_arquivos(): #Salvamento dos Produtos no TXT
    global produto_id

    arquivo_produtos = "Cadastros/cadastro_produtos.txt"
    if os.path.exists(arquivo_produtos):
        with open(arquivo_produtos, "r") as arquivo:
            for linha in arquivo:
                parts = linha.strip().split()
                if len(parts) == 4:  # Verifica se tem todas as partes necessárias
                    codigo = int(parts[0].split(":")[1])
                    desc = parts[1].split(":")[1]
                    preco = float(parts[2].split(":")[1])  
                    quantidade = int(parts[3].split(":")[1])
                    produtos[codigo] = [desc, preco, quantidade]
                    if codigo >= produto_id:
                        produto_id = codigo + 1
    
    # Carrega produtos do operador
    arquivo_operador = "Cadastros/cadastro_operador.txt" 
    if os.path.exists(arquivo_operador):
        with open(arquivo_operador, "r") as arquivo:
            for linha in arquivo:
                parts = linha.strip().split()
                if len(parts) == 4:  # Verifica se tem todas as partes necessárias
                    codigo = int(parts[0].split(":")[1])
                    desc = parts[1].split(":")[1]
                    preco = float(parts[2].split(":")[1])
                    quantidade = int(parts[3].split(":")[1])
                    operador_produtos[codigo] = [desc, preco, quantidade]

# Main - Teclas Numéricas para os Menus do Administrador e do Operador

carregar_arquivos()
while True:
    os.system("cls")
    escolha = menu()
    while escolha not in ["1", "2", "3"]:
        print("Opção inválida.")
        escolha = input("Digite uma opção válida (1 a 3): ").strip()
    
    if escolha == "1":  # Administrador
        while True:
            os.system("cls")
            escolhaADM = menuADM()
            while escolhaADM not in ["1", "2", "3", "4", "5"]:
                print("Opção inválida.")
                escolhaADM = input("Digite uma opção válida (1 a 5): ").strip()
            
            if escolhaADM == "1":
                cadastrar_produto()
            elif escolhaADM == "2":
                listar_produtos()
            elif escolhaADM == "3":
                editar_produto()
            elif escolhaADM == "4":
                excluir_produto()
            elif escolhaADM == "5":
                break
            input("Pressione Enter para continuar...")

    elif escolha == "2":  # Operador
        while True:
            os.system("cls")
            escolhaOP = menuOperador()
            while escolhaOP not in ["1", "2", "3"]:
                print("Opção inválida.")
                escolhaOP = input("Digite uma opção válida (1 a 3): ").strip()
            
            if escolhaOP == "1":
                adicionar_produto_operador()
            elif escolhaOP == "2":
                listar_produtos_operador()
            elif escolhaOP == "3":
                break
            input("Pressione Enter para continuar...")

    elif escolha == "3":
        os.system("cls")
        print("Fim da execução")
        break