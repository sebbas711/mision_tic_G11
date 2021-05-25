Horas = float(input("Ingresa horas:"))

minutos = Horas*60
Segundos = minutos*60
dias = round((Horas/24),4)

print("************* RESULTADOS *************")
print("*La cantidad de horas  :",Horas)
print("*Tiene   ",minutos," minutos")
print("*Tiene   ",Segundos," Segundos")
print("*Es   ",dias," Dias")
print("************* FIN *************")