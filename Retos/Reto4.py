def lectura_de_datos():
    Numero1, Numero2 = input().split()
    nota=[int(num) for num in list(input().split())]
    return (int(Numero1),int(Numero2),nota)
def total_copias(Numero2,nota):
    totales_c=0
    if nota.count(nota[0])==len(nota):
        totales_c=len(nota)-1
    else:
        evaluados=[]
    for i in nota:
        if (i not in evaluados):
            evaluados.append(i)
        contador=0
        contador=nota.count(i)
        if (contador>1):
            contador=contador-1
            totales_c+=contador
    return(totales_c)
def copias_detectadas(Numero2,nota):
    c_detectadas=0
    if nota.count(nota[0])==len(nota):
        c_detectadas=len(nota)-1
    else:
        a=0
        b=Numero2
    for i in range(Numero2,len(nota)):
        num=nota[a:b]
        if (nota[b] in num):
            c_detectadas+=1
        a+=1
        b+=1
    return c_detectadas
Numero1,Numero2,nota=lectura_de_datos()