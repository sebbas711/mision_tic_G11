"""El profesor del curso de fundamentos de programación necesita calcular la nota definitiva para un estudiante, el 100% de nota esta distribuida de la siguiente manera: un 30% corresponde a la nota promedio de los 3 talleres que se realizaron durante el curso, otro 30% corresponde a la nota promedio de 2 evaluaciones cortas realizadas y un 40% corresponde al proyecto final que esta comprendido por el trabajo(50%) y la sustentación del mismo(50%)"""

nombreEstudiante = input("Ingrese el nombre del Estudiante: ")

taller1 = float(input("Ingrese la nota del taller 1: "))
taller2 = float(input("Ingrese la nota del taller 2: "))
taller3 = float(input("Ingrese la nota del taller 3: "))

evaluacion1 = float(input("Ingrese la nota de la evaluación 1: "))
evaluacion2 = float(input("Ingrese la nota de la evaluación 2: "))

trabajo = float(input("Ingrese la nota del trabajo correspondiente al proyecto final: "))
sustentacion = float(input("Ingrese la nota de la sustentación correspondiente al proyecto final: "))

notaTalleres =((taller1 + taller2 + taller3)/3)*0.30
notaEvaluaciones = ((evaluacion1+evaluacion2)/2)*0.30
notaProyectoFinal = ((trabajo+sustentacion)/2)*0.40

notaDefinitiva = notaTalleres + notaEvaluaciones + notaProyectoFinal

print("La nota definitiva del estudiante: ", nombreEstudiante, " es: ", notaDefinitiva)