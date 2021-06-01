numero_usuarios = [1,2,3,4,5,6,7,8,9,10]
suma = 0
suma2 = 0

cantidad_elementos = len(numero_usuarios)

for posicion in range(0,cantidad_elementos,2):
    print(numero_usuarios[posicion])
    suma = suma + numero_usuarios[posicion]

print ("La sumatoria de las posiciones pares es: ",suma)

for posicion in range(1,cantidad_elementos,2):
    print(numero_usuarios[posicion])
    suma2 = suma2 + numero_usuarios[posicion]

print ("La sumatoria de las posiciones impares es: ",suma2)