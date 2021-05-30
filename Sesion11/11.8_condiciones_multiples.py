edad = int(input("ingresa tu edad: "))

if edad >= 18:
    print("Bienvenido al bar porque eres mayor de edad")
else:
    tiempo_restante = 18-edad
    print("No puedes ingresar al bar por favor vuelve en {tiempo_restante} años")
