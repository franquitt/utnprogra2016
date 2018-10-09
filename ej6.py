nros = [4, 24, 12, 25, 8, 14, 15, 19, 12, 17, 29, 17, 21, 21, 23, 0, 34, 26, 10, 8, 29, 4, 29, 29, 17, 27, 33, 16, 26, 7, 29, 28, 21, 21, 17, 25, 21, 20, 13, 30, 4, 0, 8, 16, 22, 15, 14, 22, 31, 13]

c = int(input("Cantidad de casos: "))
resultados = []


def calcularTipo(apuesta, estrategia):
    rojoImpar = [1, 3, 5, 7, 9, 19, 21, 23, 25, 27]
    rojoPar = [12, 14, 16, 18, 30, 32, 34, 36]
    negroImpar = [11, 13, 15, 17, 29, 31, 33, 35]
    negroPar = [2, 4, 6, 8, 10, 20, 22, 24, 26, 28]

    if (apuesta == "paridad"):
        if (estrategia == "par"):
            return (rojoPar + negroPar)
        else:
            return (rojoImpar + negroImpar)
    else:
        if (estrategia == "rojo"):
            return (rojoPar + rojoImpar)
        else:
            return (negroPar + negroImpar)


def jugar():
    pos = int(input("Numero de inicio 0-49: "))
    apuesta = input("Paridad o color: ")
    estrategia = input("Estrategia: ")
    presupuesto = int(input("Presupuesto: "))
    apuestaMax = int(input("Apuesta maxima: "))

    ap = 1

    numeros = calcularTipo(apuesta, estrategia)
    cant = 0

    salir = False
    while (not salir):
        cant += 1
        if (presupuesto == 0):
            break
        if (nros[pos] not in numeros or nros[pos] == 0):
            if (presupuesto >= ap):
                presupuesto = presupuesto - ap
            else:
                presupuesto = 0
            ap = ap * 2
            if (ap > apuestaMax):
                ap = apuestaMax
        else:
            presupuesto = presupuesto + ap
        pos = pos + 1
        if (pos >= len(nros)):
            pos = 0

    return cant



for i in range(0, c):
    resultados.append(jugar())

print(resultados)