numeros = [10,4,5,6,7,8,1,2,4,5]
ordenados = sorted(numeros) #Orgnaiza la lista de menor a mayor
print(ordenados)
print(len(numeros)) #Permite saber la cantidad de elementos que tiene la lista numeros

numeros.append(100) #agrego el numero 100 a la lista en la ultima posicion
print(numeros)

numeros.insert(2,340) #insertamos el numero 340 en la posicion 2
print(numeros)

numeros.pop(0) #eliminamos el elemnto que se encuenrte en la posicion 0
print(numeros)

del numeros[4:8] #eliminamos los elementos que se encuentren desde la posicion 4 hasta 8-1
print(numeros)

numeros.remove(4) #eliminar el primer numero 4 que encuentre en la lista 
print(numeros)

print(numeros.index(340)) #me retorna la posicion del numero 340 en la lista

numeros_no_repetidos = set(numeros)
print(list(numeros_no_repetidos))

