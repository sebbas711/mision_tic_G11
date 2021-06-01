suma_par = 0
suma_impar = 0

print("Vamos a sumar los numeros pares de 1-100")

for numeros in range(2,101,2):
    suma_par = suma_par+numeros

print(f"la suma de los numeros paeres es de 1-100 es {suma_par}")  

print("=========================================")

print("Vamos a sumar los numeros impares de 1-100")

for numeros in range(1,101,2):
    suma_impar = suma_impar+numeros

print(f"la suma de los numeros impares es de 1-100 es {suma_impar}")  