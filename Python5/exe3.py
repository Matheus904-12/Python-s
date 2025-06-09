#Elaborar uma função que retorna o cálculo do volume de uma esfera. Sendo que o raio é passado por parâmetro.

import os
os .system("cls")

raio = float(input("Qual é valor do raio da esfera: \n"))

def VE(raio):
    return 4/3 * 3.14 * (raio)**3

Resultado = VE(raio)
print(f"O Volume da Esfera é: {Resultado}")

