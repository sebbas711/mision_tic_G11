numberinit = int(input("Ingrese el numero inicial (n): "))
numberEnd = int(input(f"Ingrese el numero final (m) mayor que {numberinit}: "))

print("========================RESULTADO=========================")
print(f"Los numeros multiplos de {numberinit} entre {numberinit} y {(numberinit*numberEnd)} son:")
for number in range(numberinit, (numberinit*numberEnd)+1,numberinit):
    print(number)
print("========================FIN================================")