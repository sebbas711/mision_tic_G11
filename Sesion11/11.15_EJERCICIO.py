"""DETERMINAR LA CANTIDAD DE DINERO QUE RECIBIRA UN TRABAJADOR POR CONCEPTO DE LAS
HORAS EXTRAS TRABAJADAS EN UNA EMPRESA, SABIENDO QUE CUANDO LAS HORAS DE TRABAJO EXCEDEN
A 40, EL RESTO SE CONSIDERAN HORAS EXTRASY QUE ESTAS SE PAGAN AL DOBLE DE UNA HORA NORMAL CUANDO NO EXCEDEN 8, 
SI LAS HORAS EXCEDEN DE 8, SE PAGARAN LAS PRIMERAS 8 AL DOBLE DE LO QUE SE PAGAN LAS HORAS
NORMALES Y EL RESTO AL TRIPLE"""


salario = int(input("Ingrese valor hora:"))
horas_trabajadas = int(input("Ingrese HORAS TRABAJADAS:"))

if horas_trabajadas <=40:
    print(f"USTED NO TIENE HORAS EXTRAS POR COBRAR")

elif horas_trabajadas > 40 and horas_trabajadas <= 48:
    hora_extra_trabajada = horas_trabajadas - 40
    hora_extra_a_pagar = (salario * 2) * hora_extra_trabajada
    print(f"LAS HORAS TRABAJADAS EXTRAS FUERON: {hora_extra_trabajada}")
    print(f" Y EL VALOR A PAGAR POR CONCEPTO DE EXTRAS ES DE: {hora_extra_a_pagar}")
    print(f"..........GRACIAS POR SU COMPROMISO CON LA EMPRESA...........") 

elif horas_trabajadas > 48:
    hora_extra_trabajada = horas_trabajadas - 40
    hora_extra_a_pagar = (salario * 8) * 2
    hora_triple = horas_trabajadas - 48
    valor_hora_triple = (hora_triple * salario) * 3
    total_a_pagar = hora_extra_a_pagar + valor_hora_triple
    print(f"LAS HORAS TRABAJADAS EXTRAS FUERON: {hora_extra_trabajada}")
    print(f"Y EL VALOR A PAGAR POR CONCEPTO DE EXTRAS NO MAYOR A OCHO HORAS: {hora_extra_a_pagar}") 
    print(f"Y EL VALOR A PAGAR POR CONCEPTO DE EXTRAS MAYOR A OCHO HORAS:{valor_hora_triple}")  
    print(f"PARA UN TOTAL A PAGAR DE : {total_a_pagar}")    
    print(f"..........GRACIAS POR SU COMPROMISO CON LA EMPRESA...........") 