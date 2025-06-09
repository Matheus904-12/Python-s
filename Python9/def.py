import os
os .system("cls")

tipo = int(input("Digite o tipo do apartamento desejado (1 ou 2): "))
pessoas = int(input("Digite o número de pessoas: "))
dias = int(input("Digite o número de dias de permanência: "))

def calcular_valor_estadia(tipo_apartamento, num_pessoas, num_dias):
    if tipo_apartamento not in [1, 2]:
        return None 
    if num_pessoas > 6 or num_pessoas < 1:
        return None  

    if tipo_apartamento == 1:
        tarifas = {1: 20.00, 2: 28.00, 3: 35.00, 4: 42.00, 5: 48.00, 6: 53.00}
    else:
        tarifas = {1: 25.00, 2: 34.00, 3: 42.00, 4: 50.00, 5: 57.00, 6: 63.00}

        valor_diaria_pessoa = tarifas[num_pessoas]
        valor_total = valor_diaria_pessoa * num_pessoas * num_dias
        return valor_total

valor_a_pagar = calcular_valor_estadia(tipo, pessoas, dias)

if valor_a_pagar is not None:
    print(f"O valor total a ser pago pela família é: R$ {valor_a_pagar:.2f}")
else:
    print("Dados inválidos para o cálculo.")