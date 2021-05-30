numero_1 = int(input("ingrese el numero1: "))
numero_2 = int(input("ingrese el numero2: "))

if numero_1 == numero_2:
    resultado = numero_1*numero_2
    print(f"El resultado es: {resultado}")
else:
    if numero_1 > numero_2:
        resultado = numero_1-numero_2
        print(f"El resultado es: {resultado}")
    else:
        resultado = numero_1 + numero_2
        print(f"El resultado es {resultado}")