simbolosDef={
	"1": "E", 
		"11": "I",
			"111": "S",
				"1111": "H",
					"11111": "5",
				"1110": "V",
					"11101": "4",
					"11100": "3",
			"110": "U",
				"1101": "F",
				"1100": " ",
					"11000": "2",
		"10": "A",
			"101": "R",
				"1011": "L",
			"100": "W",
				"1001": "P",
				"1000": "J",
					"10000": "1",
	"0": "T",
		"01": "N",
			"011": "D",
				"0111": "B",
					"01111": "6",
				"0110": "X",
			"010": "K",
				"0101": "C",
				"0100": "Y",
					"01000": "7",
		"00": "M",
			"001": "G",
				"0011": "Z",
				"0010": "Q",
					"00100": "8",
			"000": "O",
				"0001": ".",
				"0000": "-",
					"00001": "9",
					"00000": "0",

}
def intToReverseBin(original):
	return str(bin(original))[2:][::-1]

def quantity(num):
	return int(num+"", 2)+1

def obtenerPalabra(numero):
	entrada=intToReverseBin(numero)
	cantletras=quantity(entrada[0:2])
	inicio=2
	texto=""
	for i in range(cantletras):
		restante=entrada[inicio:]
		nSimbolos=quantity(restante[0:2])
		restante=entrada[inicio+2:]
		simbolos = restante[0:nSimbolos]
		simbolos +="0"*(nSimbolos-len(simbolos))
		texto+=simbolosDef[simbolos]
		inicio+=2+nSimbolos
	return texto

casos = input()
frases=[]

for i in range(int(casos)):
	cantPalabras=int(input())
	palabras=[]
	for pal in range(cantPalabras):
		palabras.append(obtenerPalabra( int( input() ) ) )
	frases.append("".join(palabras))

for frase in frases:
	print(frase)