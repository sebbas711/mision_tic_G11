num1 = float(input("Ingresa Numero 1  "))
num2 = float(input("Ingresa Numero 2  "))
num3 = float(input("Ingresa Numero 3  "))
num4 = float(input("Ingresa Numero 4  "  ))

suma =num1+num2+num3+num4
resta = num1-num2-num3-num4
multiplicacion = num1*num2*num3*num4
division = round((num1/num2/num3/num4), 3)
mod12 = num1%num2
mod43 = num4%num3
exp24 = num2**num4
exp34 = num3**num4


print("************* RESULTADOS *************")
print("*La Suma de los numero es: ",suma)
print("*La Resta de los numero es: ",resta)
print("*La Multiplicación de los numero es: ",round(multiplicacion,2))
print("*La División de los numero es: ",round(division,2))
print("*El modulo de : ",num1, " y ", num2, "es : ",round(mod12,2))
print("*El modulo de : ",num4, " y ", num3, "es : ",round(mod43,2 ))
print("*",num2," Elevado a ",num4, " es: ",round(exp24,2))
print("*",num3," Elevado a ",num4, " es: ",round(exp34,2))

print("************* ADICIONAL *************")
print("*Numero ",num1, " es par : ",(num1%2)==0 )
print("*Numero ",num2, " es par : ",(num2%2)==0 )
print("*Numero ",num3, " es par : ",(num3%2)==0 )
print("*Numero ",num4, " es par : ",(num4%2)==0 )

print("*Numero ",num1, " es entero : ",(num1-round(num1,0))==0 )
print("*Numero ",num2, " es entero : ",(num2-round(num2,0))==0 )
print("*Numero ",num3, " es entero : ",(num3-round(num3,0))==0 )
print("*Numero ",num4, " es entero : ",(num4-round(num4,0))==0 )
print("************* FIN *************")