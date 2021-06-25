# Calcular los grados en decimales teniendo los grados, minutos y segundos
# Calculate the degrees in decimals having degrees, minutes and seconds

import math

grados = float(input("Ingresa los grados: "))
minutos = float(input("Ingresa los minutos: "))
segundos = float(input("Ingresa los segundos: "))

min = segundos/60 + minutos
grados_resultado = round((min/60 + grados),6)

print("El resultado en grados decimales es: ", grados_resultado)

print("\nGracias Ronald y equipo HelpGIS, mi nombre es Johanna Valenzuela")