frase = input("Digite la frase que desea verificar: ")

conteo_letras = {}

for letra in frase:
    if letra not in conteo_letras:
        conteo_letras[letra] = 1
    else:
        conteo_letras[letra]+=1

print(f"En la frase \"{frase}\" se encuentran los  siguientes caracteres\n: ")

for clave, valor in conteo_letras.items():
    print(f"letra {clave} : {valor}")