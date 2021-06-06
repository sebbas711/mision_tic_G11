def sumar(numero_1, numero_2):
    resultado_suma = numero_1 + numero_2
    return f"EL resultado es: {resultado_suma}"

def multiplicar(numero_1, numero_2):
    resultado_multiplicacion = numero_1 * numero_2
    return f"El resultado es: {resultado_multiplicacion}"

def restar(numero_1, numero_2):
    resultado_resta = numero_1 - numero_2
    return f"El resultado es: {resultado_resta}"

def dividir(numero_1, numero_2):
    resultado_division = numero_1 / numero_2
    return f"El resultado es: {resultado_division}"

print("Bienvenido a la super calculadora de fundamentos de python")

numero1=int(input("Digite el numero 1: "))
numero2=int(input("Digite el numero 2: "))

resultado_1=sumar(numero1, numero2)
print(resultado_1)
print(sumar(numero1, numero2))
print(restar(numero1, numero2))
print(multiplicar(numero1, numero2))
print(dividir(numero1, numero2))
