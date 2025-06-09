#7) Na declaração de Imposto de renda devem constar os dados: nome do contribuinte, CPF, renda anual e
#número de dependentes. Os cálculos são feitos da forma a seguir.
#Desconto de R$ 110,00 por dependente.
#Com base na renda líquida (renda anual menos descontos) é calculada a alíquota de contribuição de
#acordo com a tabela:

import os
os .system("cls")
print("Imposto de Renda")

Nome = input("Nome: ")
CPF = int(input("CPF: "))
Renda = float(input("Renda Anual: "))
Dependentes = int(input("Número de Dependentes: "))

Desconto = Dependentes * 110
print(f"Desconto: R$ {Desconto:.2f}")

Renda_Liquida = Renda - Desconto
print(f"Renda Líquida: R$ {Renda_Liquida:.2f}")

if Renda_Liquida <= 800:
    print("Isento de Imposto")
elif Renda_Liquida <= 4000:
    Imposto = Renda_Liquida * 0.025
    print(f"Imposto: R$ {Imposto:.2f}")
elif Renda_Liquida <= 9000:
    Imposto = Renda_Liquida * 0.05
    print(f"Imposto: R$ {Imposto:.2f}")
else:
    Imposto = Renda_Liquida * 0.10
    print(f"Imposto: R$ {Imposto:.2f}")