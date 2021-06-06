print("Multiplos de 6 entre 6 y 150")

DESDE = 6
HASTA = 151
num = 6
multiplos = []

for numero in range(DESDE,HASTA):
    mod = numero % num
    if mod == 0:
        multiplos.append(numero)

print(multiplos)

print("FIN DEL PROGRAMA")