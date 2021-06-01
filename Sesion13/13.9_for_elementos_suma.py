numero_usuarios = [1,2,3,4,5,6,7,8,9,10]
suma = 0
suma2 = 0

print (sum(numero_usuarios))

for numero in numero_usuarios:
    suma = suma + numero

print("La suma del primer for es", suma)

cantidad_elementos = len(numero_usuarios)

for posicion in range(cantidad_elementos):
    print(numero_usuarios[posicion])
    suma2 = suma2 + numero_usuarios[posicion]

print ("La suma del segundo for es",suma2)