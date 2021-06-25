# Calculo del area de un triangulo teniendo las coordenadas de los 3 vertices
# Calculation of the area of a triangle having the coordinates of the 3 vertices

import math

x_1 = float(input("Ingresa coordenada x del vertice 1: "))
y_1 = float(input("Ingresa coordenada y del vertice 1: "))

x_2 = float(input("Ingresa coordenada x del vertice 2: "))
y_2 = float(input("Ingresa coordenada y del vertice 2: "))

x_3 = float(input("Ingresa coordenada x del vertice 3: "))
y_3 = float(input("Ingresa coordenada y del vertice 3: "))

area = round(1/2 * abs((x_1*(y_2-y_3) + x_2*(y_3-y_1) + x_3*(y_1-y_2))),4)

print("El area del triangulo es: ", area,"m²")

print("\nGracias Ronald y equipo HelpGIS, mi nombre es Johanna Valenzuela")