frase_completa = input("Digite la frase inicial: ")

sub_cadena = input("Digite la frase que desea validar: ")

resultado = frase_completa.startswith(sub_cadena)

if(resultado):
    print(f"La frase {frase_completa} si empieza por la subcadena {sub_cadena}")
else:
    print(f"La frase {frase_completa} no empieza por la subcadena {sub_cadena}")