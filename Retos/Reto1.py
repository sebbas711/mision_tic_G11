"""Reto 1: El Salario de Pedro

es un empleado de una empresa de procesos industriales y desea conocer a cuánto dinero equivalen los descuentos de nómina exigidos por la ley en relación con los pagos que la empresa para la que trabaja le realiza mensualmente. Se ha firmado un contrato que le permite trabajar 48 horas semanales. Con el propósito de verificar el valor total de los descuentos han decidido construir un programa en Python que le permita verificar el valor de su salario antes y después de realizar los descuentos. Después de consultar sobre la normatividad y revisar con detalle su contrato laboral nota que debe tener en cuenta los siguientes aspectos:

El valor de una hora de trabajo normal se obtiene dividiendo el salario base sobre 195.
Las horas extras se liquidan con un recargo del 35% sobre el valor de una hora normal.
Debido a un buen desempeño de un empleado la empresa ocasionalmente otorga bonificaciones de 4.5% del salario base.
El salario total antes de descuentos se calcula como la suma del salario base, más el valor de las horas extras, más las bonificaciones (si las hay).
Se descontará 5.5% del salario total antes de descuentos para el plan obligatorio de salud.
Se descontará 5% del salario total antes de descuentos para el aporte a pensión.
Se descontará 5% del salario total antes de descuentos para caja de compensación.

Luego de considerar toda esta información, el empleado decide construir un programa que permita a cualquier empleado de la empresa verificar si los pagos son correctos."""

nombre = input("Ingrese por favor su nombre: ")
salario_base = float(input("ingrese su salario base: "))
valor_hora =  int(salario_base / 195)
print("El valor de la hora es de: ", round(valor_hora,2))
horas_extras = int(input("ingrese la cantidad de horas extras hechas: ")) 
if horas_extras == 0:
    print("No realizo horas extras")
elif horas_extras >= 1:
    hora_extra_total = valor_hora*0.35
    Total_extras = horas_extras*valor_hora+hora_extra_total
    print("Usted realizo: ", horas_extras, "horas extras lo que equivale a: ", round(Total_extras,2))

bonificacion = int(input("Si hizo bonificaciones ingrese el numero 1, de lo contrario ingrese el numero 0: "))

if bonificacion == 1:
    bonificacion_calculo=salario_base*0.045
    bonificacion_total=bonificacion_calculo+salario_base
    print("su bonificacion es de: ", round(bonificacion_total,2))
    salario_antes_descuentos = salario_base + Total_extras + bonificacion_total
    print("Su salario antes de los decuentos es de: ", round(salario_antes_descuentos,2))
    descuento1 = salario_antes_descuentos*0.055
    descuento2 = salario_antes_descuentos*0.05
    descuento3 = salario_antes_descuentos*0.05
    descuentos_nomina = descuento1 + descuento2 + descuento3
    salario_total = salario_antes_descuentos - descuentos_nomina
    print("Su salario total es: ", salario_total)
elif bonificacion == 0:
    print("Usted no gano bonificaciones este mes")
    salario_antes_descuentos = salario_base + Total_extras
    print("Su salario antes de los decuentos es de: ", round(salario_antes_descuentos,2))
    descuento1 = salario_antes_descuentos*0.055
    descuento2 = salario_antes_descuentos*0.05
    descuento3 = salario_antes_descuentos*0.05
    descuentos_nomina = descuento1 + descuento2 + descuento3
    salario_total = salario_antes_descuentos - descuentos_nomina
    print("Su salario total es: ", salario_total)





