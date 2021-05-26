"""Ejercicio #2: Una pequeña empresa necesita saber en cuanto puede vender el
producto que fabrica. De dicho producto conocemos el nombre, el código
y el costo de producción; es necesario que el precio de venta incluya
120% como utilidad y un 15% de impuestos."""

nombreProducto = input("Ingrese el nombre el producto: ")
codigoProducto = input("Ingrese el codigo del producto: ")
costoProduccion = int(input("Ingrese el costo de produccion: "))

utilidad = 1.20
impuestos = 0.15

precioyUtilidad = costoProduccion*utilidad
precioeImpuestos = costoProduccion*impuestos

precioTotal = costoProduccion + precioyUtilidad + precioeImpuestos

print("El precio total de", codigoProducto,".", nombreProducto, "es: ", precioTotal)