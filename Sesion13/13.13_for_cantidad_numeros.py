numero_guardados = []

numeros_almacenar = int(input("Digite la cantidad de numeros que desea almacenar: "))

while numeros_almacenar <= 0:
    print("Por favor ingrese un numero positivo")
    numeros_almacenar = int(input("Digite la cantidad de numeros que desea almacenar: "))

for contador in range(numeros_almacenar):
    numero_guardados.append(int(input(f"Digite el numero {contador+1} que desea almacenar: ")))
    
for numero in numero_guardados:
    if(numero%2==0):
        suma=suma+numero

print(f"La suma de los numeros pares es: {suma}")