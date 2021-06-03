palabra = input("Digite una palabra")
print(palabra.isdigit())

if palabra.isdigit():
    print("Felicitaciones usted ingreso un numero")
else:
    print("la información ingresada contiene caracteres diferentes a numeros")