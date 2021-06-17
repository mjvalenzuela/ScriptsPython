#Calcular descuentos de matricula a estudiantes segun edad, ingresos y puntaje de examen
#Calculate tuition discounts for students based on age, income and test scores.

print("Calculo de porcentaje de apoyo sobre el valor de la matricula\n")
nombres = input("Por favor ingrese los nombres del candidato: ")
apellidos = input("Por favor ingrese los apellidos del candidato: ")
edad = int(input("Por favor ingrese la edad del candidato: "))
puntaje = int(input("Por favor ingrese el puntaje del examen del candidato: "))
while not (0 <= puntaje <= 100):
    print("Puntaje no correcto")
    puntaje = int(input("Por favor ingrese el puntaje del examen del candidato: "))
ingresos = float(input("Por favor ingrese los ingresos familiares en SMMLV del candidato: "))

apoyoEdad = 0
apoyoIngresos = 0
apoyoPuntaje = 0
apoyoTotal = 0

if (edad >= 15 and edad <= 18):
    apoyoEdad = 25
elif (edad >=19 and edad <= 21):
    apoyoEdad = 15
elif(edad >=22 and edad <= 25):
    apoyoEdad = 10
elif(edad >=26):
    apoyoEdad = 0

if (ingresos <= 1):
    apoyoIngresos = 30
elif (ingresos >1 and ingresos <= 2):
    apoyoIngresos = 20
elif (ingresos >2 and ingresos <= 3):
    apoyoIngresos = 10
elif (ingresos >3 and ingresos <= 4):
    apoyoIngresos = 5
elif (ingresos > 4):
    apoyoIngresos = 0

if (puntaje >=80 and puntaje < 86):
    apoyoPuntaje = 30
elif (puntaje >=86 and puntaje < 91):
    apoyoPuntaje = 35
elif (puntaje >=91 and puntaje < 96):
    apoyoPuntaje = 40
elif puntaje >=96:
    apoyoPuntaje = 45
elif puntaje < 80:
    apoyoPuntaje = 0

apoyoTotal = apoyoEdad + apoyoIngresos + apoyoPuntaje

print("\n\n********** RESULTADOS ********** \n")
print("\nNombre completo del beneficiario es: " + nombres + " " + apellidos)
print("El descuento aplicado por edad es: " + str(apoyoEdad) + "%")
print("El descuento aplicado por ingresos es: " + str(apoyoIngresos) + "%")
print("El descuento aplicado por puntaje es: " + str(apoyoPuntaje) + "%")
print("El descuento total aplicado al valor de la matricula es: " + str(apoyoTotal) + "%\n")

nombres_carrera = ("Sistemas", "Musica", "Medicina")
valores_carrera = (6500000,3500000,12000000)

for carrera in nombres_carrera:
    valor_carrera = valores_carrera[(nombres_carrera.index(carrera))]
    valor_pagar = valor_carrera * (1-apoyoTotal/100)

    print("El valor de la carrera %s con el descuento aplicado es de $%s " %(carrera,round(valor_pagar,0)))






