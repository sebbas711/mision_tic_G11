"""debido a la gran cantidad de conductores que infringen los límites de velocidad en Cundinamarca, la Gobernaciónha decidido implementar controles que cumplieron sancionara a aquellos conductores que no respeten los límites de velocidad establecidos en las vías del departamento. Con este fin, la Gobernación ha decidido instalar radares de tramo en las carreteras con mayor índice de infractores

Los radares de tramo funcionan colocando dos cámaras en dos puntos alejados de una carretera con el fin de comprobar cuánto tiempo tarda un conductor recorrer dicho tramo. Estos radares no mide la velocidad de paso, sino el tiempo de paso representado como la velocidad media de un conductor en un trayecto con una longitud determinada.

Formalmente, los radares de tramo se basan en el teorema de Lagrange (también conocido como el teorema de valor medio o de Bonnet-Lagrange), el cual nos dice que dice tenemos una función continua en un intervalo cerrado, y derivable en un intervalo abierto , entonces algún punto de ese intervalo abierto la función tendrá una derivada instantánea igual a la pendiente media de la curva en el intervalo cerrado.

Aunque estos conceptos pueden asustar en un principio, su interpretación es muy simple: si hacemos un viaje desde Bogotá a Tunja y nuestra velocidad media es de 100 Km / h, necesariamente en algún punto del trayecto nuestra velocidad habrá sido de 100 Km / h. Esto quiere decir que si la velocidad media supera la velocidad máxima permitida, gracias al teorema anterior, sabremos que en algún punto del trayecto se superó la velocidad máxima permitida. Por ejemplo, si colocamos las cámaras separadas 10 Km en un tramo cuya velocidad máxima es de 110 Km / h, y un conductor tarda 5 minutos en ser visto por la segunda cámara, sabremos que su velocidad media ha sido de 120 Km / h, y por tanto, en algún sitio ha superado la velocidad permitida.

Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los datos registrados por las cámaras. Su misión es crear un programa en Python que permita saber si un conductor debe ser multado o no."""

distancia = 0
velocidad_maxima = 0
tiempo = 0

distancia, velocidad_maxima, tiempo = (input()).split()

distancia = int(distancia)
velocidad_maxima = int(velocidad_maxima)
tiempo = int(tiempo)

velocidad_carro = distancia / tiempo

velocidad_carro = velocidad_carro * 3600 / 1000


if velocidad_carro <= velocidad_maxima:
    print("OK")
elif distancia < 0 or velocidad_maxima < 0 or tiempo < 0:
    print("VALORES NEGATIVOS")
elif velocidad_carro > velocidad_maxima and velocidad_carro < (velocidad_maxima * 1.25):
    print("MULTA")
elif velocidad_carro > (velocidad_maxima*1.25):
    print("CURSO SENSIBILIZACION")
