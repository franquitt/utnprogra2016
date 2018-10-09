c = int(input("Cantidad de casos: "))
resultados = []
posicion = 0


def mover(grad):
    global posicion
    posicion += grad
    if (posicion > 360):
        posicion = posicion + 360
    if (posicion < 0):
        posicion = 360 + posicion


def aproximar():
    global posicion
    if (0 <= posicion < 11.250 or 348.75 <= posicion <= 359):
        return("N")
    if (11.250 <= posicion < 33.75):
        return("NNE")
    if (33.75 <= posicion < 56.250):
        return("NE")
    if (56.25 <= posicion < 78.75):
        return("ENE")
    if (78.75 <= posicion < 101.250):
        return("E")
    if (101.250 <= posicion < 123.750):
        return("ESE")
    if (123.75 <= posicion < 146.250):
        return("SE")
    if (146.250 <= posicion < 168.750):
        return("SSE")
    if (168.750 <= posicion < 191.25):
        return("S")
    if (191.25 <= posicion < 213.75):
        return("SSO")
    if (213.75 <= posicion < 236.25):
        return("SO")
    if (236.25 <= posicion < 258.75):
        return("OSO")
    if (258.75 <= posicion < 281.25):
        return("O")
    if (281.25 <= posicion < 303.75):
        return("ONO")
    if (303.75 <= posicion < 326.25):
        return("NO")
    if (326.25 <= posicion < 348.75):
        return("NNO")


for i in range(0, c):
    g = int(input("Cantidad de movimientos: "))
    for i in range(0, g):
        movimiento = input("Ingrese movimiento: ")
        direccion = movimiento[0:1]
        grados = int(movimiento[2:len(movimiento)])
        if (direccion == "e" or direccion == "E"):
            mover(grados)
        if (direccion == "b" or direccion == "B"):
            mover(-grados)
    resultados.append(aproximar())
    posicion = 0

for r in resultados:
    print(r)
