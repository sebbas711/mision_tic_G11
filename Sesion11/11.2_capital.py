"""Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto dinero ganara despues de un mes si el banco paga razon de 15% efectivo anual"""

INTERES_ANUAL = float(input("Ingrese la tasa de interes efectivo anual"))
INTERES_MENSUAL = INTERES_ANUAL / 12

capital = float(input("Por favor ingrese el capital que desea invertir: "))
numero_meses = int(input("Por favor ingrese el numero de meses que desea invertir el dinero: "))
rendimiento = capital*INTERES_MENSUAL*numero_meses
capital_final=capital+rendimiento

print(f"El rendimiento de su inversion despues de un mes es {rendimiento:.2f}")
print(f"El saldo final proyectado es de: {capital_final:.2f}")