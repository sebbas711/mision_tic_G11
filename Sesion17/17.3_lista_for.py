"""Programa que permita ingresar 10 numeros
me imprima el promedio de los numeros ingresados 
me imprima el mayor y el menor
que me genere una lista con los pares y otro con los impares."""

total = 0
numero_ingresado = []
pares = []
impares = []

for numero in range(10):
    mensaje = f"ingrese el {numero+1} que desea almacenar"
    numero_ingresado = int(input(mensaje))
    numero_ingresado.append(numero_ingresado)

for numero in numero_ingresado:
    total+=numero
    if numero %2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

promedio = total/len(numero_ingresado)
menor = min(numero_ingresado)
mayor = max(numero_ingresado)

print(f"El promedio de los numeros ingresados es {promedio}")
print(f"el numero menor en la lista de numeros ingresados es: {menor}")
print(f"el numero mayor en la lista de numeros ingresados es: {mayor}")
print(f"Los numeros pares que hay en la lista de numeros ingresados son {pares}")
print(f"Los numeros impares que hay en la lista de numeros ingresados son {impares}")