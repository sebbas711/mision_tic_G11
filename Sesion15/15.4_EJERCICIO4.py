frase = input("Ingrese la cadena que desea validar: ")
caracter1 = input("Ingrese caracter que desee que validemos : ")

while not(caracter1.isalpha()) or len(caracter1)>1:
    print("No se registro correctamente el caracter, recuerde que debe ingresar solo una letra")
    caracter1 = input("Ingrese caracter que desee que validemos : ")

caracter2 = input("Ingrese caracter que desee que validemos : ")

while not(caracter2.isalpha()) or len(caracter2)>1:
    print("No se registro correctamente el caracter, recuerde que debe ingresar solo una letra")
    caracter2 = input("Ingrese caracter que desee que validemos : ")


resultado = frase.replace(caracter1, caracter2, 4)
print(resultado)