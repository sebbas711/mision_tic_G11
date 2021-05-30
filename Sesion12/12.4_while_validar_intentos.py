MAXIMOS_INTENTOS = 3
password = "1234"
contador = 0

intento = input("ingrese su contraseña: ")

if(intento == password):
    print("Transacción exitosa")
else:
    while(contador<MAXIMOS_INTENTOS):
        intento = input("ingrese su contraseña: ")
        if intento == password:
            print("Transacción exitosa")
            break
        contador+=1

print("bloqueo su cuenta")

