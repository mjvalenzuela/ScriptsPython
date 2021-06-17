#Calculos de temperaturas minimas y maximas segun registros ingresados
#Calculations of minimum and maximum temperatures based on entered records

print("\nBIENVENIDO AL REGISTRO DE DATOS DIARIOS DE TEMPERATURA\n")
print("Ingrese los registros de temperatura (para finalizar ingrese 0): \n")

ambos_error = 0
min_error = 0
max_error = 0
total_min = 0
total_max = 0
promedio_min = 0
promedio_max = 0
dias_error = 0
porcentaje = 0

registro = ()
listado_temperaturas = []
dia=0

while True:
    try:
        temp_min = float(input("Ingrese temperatura MINIMA para el día " + str(dia+1) + ": "))
        temp_max = float(input("Ingrese temperatura MAXIMA para el día " + str(dia+1) + ": "))
        registro = (temp_min,temp_max)
        print("\n")

        while registro != (0,0):

            dia+=1
            listado_temperaturas.append(registro)
            temp_min = float(input("Ingrese temperatura MINIMA para el día " + str(dia+1) + ": "))
            temp_max = float(input("Ingrese temperatura MAXIMA para el día " + str(dia+1) + ": "))
            registro = (temp_min,temp_max)
            print("\n")

        for reg in listado_temperaturas:
            print(reg)
            if reg[0] < 5 and reg[1] > 35:
                ambos_error += 1
                dias_error += 1
            elif reg[0] < 5:
                min_error += 1
                dias_error += 1
            elif reg[1] > 35:
                max_error += 1
                dias_error += 1

            total_min = total_min + reg[0]
            total_max = total_max + reg[1]

        promedio_min = total_min/dia
        promedio_max = total_max/dia
        porcentaje = (dias_error/dia)*100

        print("\n***************** RESULTADOS *****************")
        print("Total dias de salida de campo = " + str(dia))
        print("Total días con temperatura minima menor a 5 y maxima mayor a 35 = " + str(ambos_error))
        print("Total días con temperatura minima menor a 5 = " + str(min_error))
        print("Total días con temperatura maxima mayor a 35 = " + str(max_error))
        print("La temperatura media minima es = " + str(format(promedio_min, '.2f')))
        print("La temperatura media maxima es = " + str(format(promedio_max, '.2f')))
        print("El porcentaje de dias reportados con errores = " + str(format(porcentaje, '.2f')) + "%\n\n")

        break

    except ValueError:
        print("Debe ingresar solo numeros")
        continue