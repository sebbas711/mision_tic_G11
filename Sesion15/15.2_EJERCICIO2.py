frase = input("Ingrese la cadena que desea validar: ")
caracter = input("Ingrese caracter que desee que validemos validar: ")

while not(caracter.isalpha()) or len(caracter)>1:
    print("No se registro correctamente el caracter que ya es superior a una letra")
    caracter = input("Ingrese caracter que desee que validemos validar: ")

resultado = frase.count(caracter)

print(f"En la frase se encontró {caracter}: {resultado} veces")