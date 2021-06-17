#Calculo de pagos y descuentos de nomina teniendo el numero de horas y valor hora
#Calculation of payments and payroll deductions taking into account the number of hours and hourly value

nombre = input("Ingrese nombre del docente: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = int(input("Ingrese el valor de la hora: "))

def cal_sueldo_bruto(horas,valor):
    if horas <= 40:
        valor_normal = horas * valor
        valor_adicionales = 0
    else:
        valor_normal = 40 * valor
        valor_adicionales = (horas-40)*(valor*1.5)
    valor_total = valor_normal + valor_adicionales
    return valor_normal,valor_adicionales,valor_total

def cal_descuentos(sueldo_br):
    des_parafiscales = sueldo_br*0.09
    des_salud = sueldo_br*0.04
    des_pension = sueldo_br*0.04
    return des_parafiscales,des_salud,des_pension

def cal_sueldo_neto(sueldo_br):
    total_descuentos = sueldo_br-parafiscales-salud-pension
    return total_descuentos

def cal_provisiones(sueldo_br):
    prov_prima = sueldo_br*0.0833
    prov_cesantias = sueldo_br*0.0833
    prov_int_cesantias = sueldo_br*0.01
    prov_vacaciones = sueldo_br*0.0417
    return prov_prima,prov_cesantias,prov_int_cesantias,prov_vacaciones

valor_sueldo_normal, valor_horas_adicionales, sueldo_bruto = cal_sueldo_bruto(horas_trabajadas,valor_hora)
parafiscales,salud,pension = cal_descuentos(sueldo_bruto)
sueldo_neto = cal_sueldo_neto(sueldo_bruto)
prima,cesantias,int_cesantias,vacaciones = cal_provisiones(sueldo_bruto)

print("Valor horas normales: " + str(valor_sueldo_normal))
print("Valor horas adicionales: " + str(valor_horas_adicionales))
print("Sueldo bruto: $" + str(sueldo_bruto))
print("Descuento por parafiscales: $" + str(parafiscales))
print("Descuento por salud: $" + str(salud))
print("Descuento por pension: $" + str(pension))
print("Descuentos totales: " + str(parafiscales+salud+pension))
print("Sueldo neto: $" + str(sueldo_neto))
print("Provision para Prima: $" + str(prima))
print("Provision para Cesantias: $" + str(cesantias))
print("Provision para Intereses sobre cesantias: $" + str(int_cesantias))
print("Provision para Vacaciones: $" + str(vacaciones))