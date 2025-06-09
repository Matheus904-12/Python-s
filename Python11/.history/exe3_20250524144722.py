import os
os .system("cls")

#Variáveis

confirm = "s"
confirmar = "s"
produtos = {}
produto_id = 100

#Funções

#Menu Inicial
def menu():
    print("1) Administrador")
    print("2) Operador")
    print("3) Sair")
    option = str(input("Digite qual opção deseja (escreva um número de 1 a 3).")).strip()
    while option == "" and option != "1" and option != "2" and option != "3":
        option = str(input("Por favor, digite um número correto (de 1 a 3): "))

    return option

#Menu do ADM
def menuADM():
    print("\n1) Cadastrar")
    print("2) Listar")
    print("3) Editar")
    print("4) Excluir")
    print("5) Voltar")
    optionadm = str(input("Escolha uma opção de 1 a 5: ")).strip()
    while optionadm not in ["1", "2", "3", "4", "5"]:
        optionadm = str(input("Digite uma opção correta!")).strip()
    return optionadm

#Menu do Operador
def munuOperador():
    print("\n1) Adicionar produto á conta")
    print("2) Listar meus produtos")
    print("3) Voltar")
    optionop = str(input("Escolha uma opção de 1 a 3: ")).strip()
    while optionop not in ["1", "2", "3"]:
        optionop = str(input("Digite uma opção correta!")).strip()
    return optionop

#Cadastro de Produto
def cadastroProduto():
    global produto_id
    desc = str(input("Digite a descrição do produto: ")).strip()
    while not desc:
        desc = str(input("Descrição Inválida!")).strip()

    try:
        preco = float(input("Digite o preço do produto: "))
        while preco <= 0:
            preco = float(input("Preço Inválido!"))
    except ValueError:
        print("Erro!")
        return
    
    produtos[produto_id] = [desc, preco]
    print(f"produto cadastrado com sucesso! Código: {produto_id}")
    produto_id += 1
    salvar_arquivo()

#Listar Dados
def listar(): #Essa foi complicada.
    arquivo = open("exe3/cadastro.txt", "r")
    listar = arquivo.readlines() #Irá ler linha por linha
    arquivo.close()

    if len(listar) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for linha in listar: #Ponteiro para a repetição
            start_fulano = linha.find("nome:") + len("nome:") #Acha a palavra nome, tem indice 0, por isso coloquei + len("nome"), quero saber o nome do aluno, não "nome:fulano". Poderia ter colocado só 5 também, mas ficaria menos escalavel.
            end_fulano = linha.find("e-mail:") #Vai achar o índice do email, ou seja, quando ele começa
            name = linha[start_fulano:end_fulano].strip() #O professor ensinou esse método em sala da aula, ele vai do ponto A até o B da lista, no caso, onde começa o nome e onde começa o email. Eu não sei se o professor ensinou o strip em sala de aula, mas eu vi isso naquele desafio da Erika junto com o Luigi :D
            print(name) #Vai retornar o nome do aluno

#def editar():
    print("editar")

#def buscar():
    arquivo = open("exe3/cadastro.txt", "r")
    listar = arquivo.readlines() #Vai ler o arquivo todo
    arquivo.close()

    searchFulano = str(input("Digite o nome do aluno que quer buscar: ")).strip() #input
    encontrado = False #A priori, falso, o código vai falar se é verdadeiro

    for linha in listar: #Vai procurar na linha toda
        if f"nome:{searchFulano}" in linha: #Se o nome estiver em linha: encontrado
            print("Aluno encontrado! \n")
            print(linha)
            encontrado = True #Se verdadeiro, o encontrado se torna True e passa direto pelo if not
            break

    if not encontrado: #inverte o valor da condição, aqui seria verdadeiro, pois o aluno não foi encontrado, então inverti para que se o código for verdadeiro, ele passa direto, se for falso ele vai pra cá, estava colando isso no for, estava errado.
        print("Aluno não encontrado.")

#def remove():
    arquivo = open("exe3/cadastro.txt", "r")
    listar = arquivo.readlines()
    delete = str(input("Digite o nome do aluno que você quer deletar: ")).strip()
    encontrado = False 
    nova_linhas = []

    for linha in listar:
        if f"nome:{delete}" in linha:
            print("Aluno encontrado! \n")
            sure = str(input("Você tem certeza que deseja apagar o usuário? (s/n): ")).strip().lower()
            if sure == "s":
                print("aluno removido com sucesso \n")
                encontrado = True
            else:
                print("Compreensível, tenha um bom dia. \n")
                nova_linhas.append(linha)

        else:
            nova_linhas.append(linha)

    if not encontrado:
        print("Aluno não encontrado. \n")

    arquivo = open("exe3/cadastro.txt", "w")
    arquivo.writelines(nova_linhas)

    arquivo.close()

#def salvar_arquivo():
#   while open("exe3/cadastroProdutos.txt", "w") as arquivo:
#       for codigo, info in produtos.items():
#           arquivo.write(f'código:{codigo} desc:{info[0]} preco:{info[1]}\n')

#Main

while confirm == "s":

    escolha = menu() # mostrará o menu, e o resultado virará uma variável

    if escolha == "1": #dependendo da escolha o comando irá fazer algo
        print("A opção desejada foi de ADM \n")
        escolhaADM = menuADM()
        while confirmar == "s":
            if escolhaADM == "1":
                cadastroProduto()
                print("funcionou")
                confirmar = "n"

            elif escolhaADM == "2":
                #listar()
                print("funcionoiu")
                confirmar = "n"

            elif escolhaADM == "3":
                #editar()
                print("funcionoiu")
                confirmar = "n"

            elif escolhaADM == "4":
                #remove()
                print("funcionoiu")
                confirmar = "n"

            elif escolhaADM == "5":
                confirmar = "n"
                #escolha()
                print("funcionou")
                confirmar = "n"
            else:
                print("[ERRO] Dígito inválido \n")
                confirmar = "n"

    elif escolha == "2":
        print("A opção desejada foi de Operador \n")
    elif escolha == "3":
        print("Fim da execução")
    else:
        print("[ERRO] Dígito inválido \n")


    