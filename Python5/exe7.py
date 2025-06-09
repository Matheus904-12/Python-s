#7) Elaborar uma função (com retorno) que determina se um número passado como parâmetro é primo. A função quando chamada retorna 1 indicando que o número é primo e 0 caso contrário.

num1 = int(input("Digite um número \n"))

def primo(num1):
    if num1 % 2 == 0 or num1 % 3 == 0 or num1 % 5 == 0:
        return 0
    else:
        return 1
    
resultado = primo(num1)

print(f"O seu número é {resultado}")

