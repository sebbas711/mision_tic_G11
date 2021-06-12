contador = 1
clientes = {
    1234: ["Camilo","Molano", "Bogota"],
    4567: ["Alejandro","Herrera", "Cali"],
    8901: ["Daniel","Gomez", "Tunja"],
    1234: ["Pilar","Diaz", "Medellin"]
}

resultado = clientes[1234]
print(resultado)
print(clientes[1234][2])

"""ERROR de clave porque no esta en el diccionario
resultado = clientes[9999]
print(resultado)"""

resultado = clientes.get(1234)
if(resultado):
    print(f"Cliente encontrado, esta es su información {resultado}")
else:print("Cliente no encontrado")

resultado = clientes.get(999)
if(resultado):
    print(f"Cliente encontrado, esta es su información {resultado}")
else:print("Cliente no encontrado")

print(len(clientes))

cedulas = tuple(clientes.keys())
print(cedulas)

informacion = tuple(clientes.values())
print(informacion)

for cliente in clientes:
    print(cliente)

for cliente in clientes.values:
    for datos in cliente:
        print(datos.upper(), sep ="", end =" ")
    print()

#nombre, cedula, edad = input().split()

for clave, valor in clientes.items():
    print(f"Esta es la cedula del cliente {contador} {clave} y esta es su informacion {valor}")
    contador+=1