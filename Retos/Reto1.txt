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

salario_base, Cantidad_horas_extra, bonificacion = input("").split()

salario_base=float(salario_base)
Cantidad_horas_extra = int(Cantidad_horas_extra)
bonificacion=float(bonificacion)

descuento_salud = 0.055
descuento_pension = 0.05
descuento_caja = 0.05

Valor_hora = salario_base/195
Hora_extra = (Valor_hora * 0.35) + Valor_hora

if bonificacion == 1:
    bonificacion = salario_base * 0.045
elif bonificacion == 0:
    bonificacion = 0

salario_total_antes = salario_base+(Cantidad_horas_extra*Hora_extra)+bonificacion 

salario_total = salario_total_antes - ((descuento_caja*salario_total_antes)+(descuento_pension*salario_total_antes)+(descuento_salud*salario_total_antes))  

print(f"{salario_total:.1f} {salario_total_antes:.1f}")