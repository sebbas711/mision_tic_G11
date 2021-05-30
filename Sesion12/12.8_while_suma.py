suma = 0
mensaje = {"ingrese los numeros que desea sumar"}

while suma <= 100:
    numero = int(input(mensaje))
    suma = suma+numero

print("La suma de los numeros ingresados es", suma)