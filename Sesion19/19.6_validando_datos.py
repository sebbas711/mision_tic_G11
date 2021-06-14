edad = 0

def recibir_data():
    global edad

    while True:
        try:
            edad= int(input("Digite su edad"))
        except ValueError:
            print("Por Favor verifique que todos los datos ingresados sean de tipo numerico")
        else:
            print("===================Informacion ingresada correctamente========================")
            break
        finally: ("Aca finaliza este bloque")

print(edad)
recibir_data()
print(edad)
