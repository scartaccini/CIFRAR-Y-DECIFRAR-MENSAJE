from palabra_secreta import ingresoSecreto
from palabra_secreta_ordenada import creaDiccionario
from mensaje_sin_cifrar import ingresoMensaje

def codificar(x):
	
	for filas in mensajeLista:
		for c,v in numeroSecreto.items():
			if v==x:
				#mensajeFinal.append((filas[c-1]))
				mensajeFinal.append(filas[c-1])
#recorre los segmentos y palabra secreta odrenada-según el diccionario-diccionarioOrdenado- y los machea
# HOLAQ,UETAL,COMOE,STAS@ --->>> {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 
#ejm, LTMA,HUCS,AAOS,QLE@,OEOT y lo almacena en la lista mensajeFinal

def mensajeSegmentar():
	
	inicio=0
	longitud=len(clave)
	incremento=longitud
	for m in range(0,len(mensaje),len(clave)):
		mensajeLista.append(mensaje[inicio:longitud])
		inicio=longitud
		longitud += incremento
#recorre el texto a cifrar en segmentos del tamaño de la palabra secreta
#esos segmentos se guardan en una variable tipo lista, mensajeLista
#ejm, HOLAQ,UETAL,COMOE,STAS@	
	for x in range(incremento+1):
		codificar(x)
#llama al metodo codificar-pasa del 1 al tamaño de la palabra secreta- la cantidad de veces el tamaño de la palabra secreta
#['L', 'T', 'M', 'A', 'H', 'U', 'C', 'S', 'A', 'A', 'O', 'S', 'Q', 'L', 'E', '@', 'O', 'E', 'O', 'T'] se convierte en LTMAHUCSAAOSQLE@OEOT
#convierte de lista a str
	print("Mensaje cifrado: ", "".join(mensajeFinal))
#imprime el mensaje cifrado, ejm: LTMAHUCSAAOSQLE@OEOT


clave=ingresoSecreto()
numeroSecreto=creaDiccionario(clave)
mensaje=ingresoMensaje(clave)
mensajeFinal=[]
mensajeLista=[]
mensajeSegmentar()
########
######## decifrar mensaje
'''clave=ingresoSecreto()
numeroSecreto=creaDiccionario(clave)


desde=0
hasta=int(len(mensajeFinal)/len(clave))
decifrado={}
for num in range(1,len(clave)+1):
	decifrado[num]=mensajeFinal[desde:hasta*num]
	desde=hasta*num
	
for c,v in numeroSecreto.items():
	print(decifrado[numeroSecreto[c]])'''












