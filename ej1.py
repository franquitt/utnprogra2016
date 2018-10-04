import math

def numeral(numero):
	if numero==1 or numero ==0:
		return 1
	return numero*numeral(numero-1)
def ecalculado(exponente, presicion):
	n=0
	resultado=0
	while n< presicion:
		resultado+=(exponente ** n )/ float(numeral(n))
		n+=1
	return resultado

casos=int(input(""))
resultados=[]
for caso in range(casos):
	entrada=input("").split(" ")
	exponente=int(entrada[0])
	presicion=int(entrada[1])
	rangoa=int(entrada[2])
	rangob=int(entrada[3])
	exponenciado = ecalculado(exponente, presicion)
	fragmento=str(exponenciado).split(".")[1][rangoa-1:rangob]
	sumatoria=0
	for i in fragmento:
		sumatoria+=int(i)
	resultados.append(sumatoria)
for resultado in resultados:
	print(resultado)