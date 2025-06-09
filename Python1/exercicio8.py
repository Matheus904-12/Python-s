#8)Criar um algoritmo que converta segundos em minutos e segundos. Por exemplo, 252 segundos equivalem a 4 minutos e 12 segundos.

import os
os .system("cls")
total_segundos = int(input("Digite o total de segundos: "))
minutos = total_segundos // 60
segundos_restantes = total_segundos % 60
print(total_segundos,"segundos equivalem a:", minutos, "minutos e", segundos_restantes, "segundos.")