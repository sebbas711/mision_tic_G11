"""Solicitar al usuario que ingrese una lista de numeros, digite x para finalizar y que ingrese un numero que desea limite, con ese limite desea saber cuales numeros que hay menor que este en la lista original y generar una lista con esos numeros"""

numero = 0
numeros_ingresados = []
numeros_menores = []

while numero != "x":
    numero = input("Digite el numero que desea almacenar: ")
    numeros_ingresados.append(numero)

print("==============DATOS INGRESADOS CORRECTAMENTE================")
del numeros_ingresados[-1]

limite = int(input("Digite el numero que desea validar: "))

for elemento in numeros_ingresados:
    if(int(elemento) < limite):
        numeros_ingresados.append(int(elemento))

print(f"Los numeros menores que {limite} son {numeros_menores}")