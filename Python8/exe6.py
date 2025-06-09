import os
os .system("cls")

def calcular_consumo_carros():
  
  modelos = []
  consumos = []

  for i in range(5):

    modelo = input(f"Digite o modelo do {i+1}º carro: ")

    modelos.append(modelo)

    while True:

      try:

        consumo = float(input(f"Digite o consumo (km/l) do {modelo}: "))

        if consumo > 0:

          consumos.append(consumo)
          break

        else:

          print("O consumo deve ser um valor positivo.")

      except ValueError:

        print("Por favor, digite um número válido para o consumo.")

  mais_economico_indice = consumos.index(max(consumos))
  modelo_mais_economico = modelos[mais_economico_indice]

  print(f"\nO modelo de carro mais econômico é: {modelo_mais_economico} ({consumos[mais_economico_indice]} km/l)")

  print("\nConsumo de combustível para 1000 km por carro:")

  for i in range(5):

    litros_necessarios = 1000 / consumos[i]

    print(f"{modelos[i]}: {litros_necessarios:.2f} litros")

calcular_consumo_carros()
