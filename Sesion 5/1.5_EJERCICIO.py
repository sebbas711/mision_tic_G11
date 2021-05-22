"""Realizar un programa que simule a una persona que saluda a otra persona, deben solicitar que el usuario ingrese nombre, apellido, edad, comida favorita y color favorito. El sistema debe imprimir dos mensajes, el primero saludando al usuario y el segundo diciendo algun comentario referente a la comida y al color ingresado"""

print ("Manejo de información de entrada con python")
print ("-------------------------------------------")

nombre = input("Por favor ingrese su nombre: ") #Guardo la información ingresada por teclado en la variable primer_nombre
apellido = input("Por favor ingrese su apellido: ") #Guardo la información ingresada por teclado en la variable apellido
edad = int(input("Por favor ingrese edad: ")) #Guardo la información ingresada por teclado en la variable edad
comida_favorita = input("Por favor ingrese cual es su comida favorita: ") #Guardo la información ingresada por teclado en la variable comida favorita
color_favorito = input("Por favor ingrese cual es su color favorito: ") #Guardo la información ingresada por teclado en la variable color favorito

print("Bienvenido", nombre, apellido, "es un gusto saludarte")
print("veo que tienes", edad, "años de edad, y tu comida favorita es:", comida_favorita, "y el color favorito es: ", color_favorito)
