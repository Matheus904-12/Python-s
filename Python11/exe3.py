import os
os .system("cls")

#Menu

def main():
    while True:
        print("\n1) Cadastrar Novo Aluno")
        print("2) Listar Alunos")
        print("3) Buscar Alunos")
        print("4) Remover Aluno")
        print("5) Sair")

        opcao = input("O que você deseja?")

        if opcao == '1':
            cadastrarAlunos()
        elif opcao == '2':
            listarAlunos()
        elif opcao == '3':
            buscarAlunos()
        #elif opcao == '4':
            #emoverAlunos()
        elif opcao == '5':
            print("Até logo!")
            break
        else:
            print("Opção Inválida")


#Funções


def cadastrarAlunos(): #Cadastro de Alunos
    nome = input("Nome do Aluno: ")
    email = input("Email do Aluno: ")
    curso = input("Curso do Aluno: ")

    with open("exes/alunos.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {email} e {curso}\n")
    print(f"Aluno '{nome}' cadastrado com sucesso!")



def listarAlunos(): #Listagem de Alunos
    try:
        with open("exes/alunos.txt", "r") as arquivo:
            alunos = arquivo.readline()
            if not alunos:
                print("Nenhum aluno cadastrado ainda!")
            else:
                for linha in alunos:
                    nome, email, curso = linha.strip().split(',')
                    print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
    except FileNotFoundError:
        print("Nenhum aluno cadastardo ainda!")



def buscarAlunos(): #Buscar Alunos
    termo = input("Buscar por nome ou email: ").lower()
    encontrado = False
    try:
        with open("exes/alunos.txt", "r") as arquivo:
            alunos = arquivo.realines()
            for linha in alunos:
                nome, email, curso = linha.strip().split(',')
                if termo in nome.lower or termo in email.lower(): 
                    print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
        encontrado = True
    except FileNotFoundError:
        print("Nenhum aluno cadastardo ainda!")

#def removerAlunos(): #Remover Alunos