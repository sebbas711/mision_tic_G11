frase="Bienvenido a una NUEVA sesion del curso de Python"

print(frase)
print(type(frase))

print(frase.upper()) #Combierte todo a mayuscula
print(frase.lower()) #Combierte todo a minuscula
print(frase.title()) #Me retorna la primera letra en mayuscula
print(frase.lower().replace("python","cocina"))

palabra5 = "perro"
print(palabra5 == "Perro".lower())

palabras = frase.split() #Retorna una lista con los elementos que estan en el string y las separa por el espacio en blanco

print(palabras)

for palabra in palabras:
    if len(palabra)>1:
        print(palabra.capitalize(), end =" ") #Capitalize me retorna a primera letra en mayuscula
    else:
        print(palabra, end =" ")

palabras = frase.split() #Retorna una lista con los elementos que estan en el string y las separa por el espacio en blanco

print(palabras)
print("*".join(palabras)) #me genera un string con los elementos que se encuentren en la lista que le paso como parametro y los separa con el string que se encuentra en las comillas