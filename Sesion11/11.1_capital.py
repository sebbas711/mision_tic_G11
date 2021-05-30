"""Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto dinero ganara despues de un mes si el banco paga razon de 15% efectivo anual"""

INTERES_ANUAL = 0.15
INTERES_MENSUAL = INTERES_ANUAL / 12

capital = float(input("Por favor ingrese el capital que desea invertir: "))
rendimiento = capital*INTERES_MENSUAL

print(f"El rendimiento de su inversion despues de un mes es {rendimiento:.2f}")