"""Cada estudiante propone 1 ejercicio donde realice las etapas de
definición del problema y el análisis. Suscripcion a Netflix"""

print("===============================================================================================================================")
print("===========================||           NETFLIX       ||=======================================================================")
print("===============================================================================================================================")

nombreCliente = input("Hola, gracias por tu interes en nuestros servicios. Por favor ingresa tu nombre: ")
print("==============================================================")
print("Hola, ", nombreCliente, "Estos son los planes que ofrece Netflix: \n PLAN PREMIUM  por 6 meses: $300 + IVA ó por 12 meses el precio es: $550 mas IVA \n PLAN BASICO por 6 meses: $200 mas IVA  ó por 12 meses el precio es: $350 mas IVA ")
print("==============================================================")
planSeleccionado = input("Ingrese el plan deseado: ")
tiempoPlan = input("Ingrese el tiempo deseado: ")
precioPlan = int(input("Ingrese el precio del plan:$"))


iva = 0.15

PrecioIva = precioPlan*iva

precioTotal = precioPlan + PrecioIva

print("==============================================================")

print(nombreCliente, "el precio total del plan:", planSeleccionado, "Por un tiempo maximo de",tiempoPlan, "es:$", precioTotal)

print("===============================================================================================================================")
print("===========================||           NETFLIX       ||=======================================================================")
print("===============================================================================================================================")