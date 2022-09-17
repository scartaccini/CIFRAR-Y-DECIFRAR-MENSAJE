def creaDiccionario(clave):
	
	contador=1
	contadorDos=1
	contadorTres=1
	diccionario={}
	diccionarioOrdenado={}
	diccionarioClave={}
	#recorre la palabra secreta,ejem F,U,E,G,O y la guarda en variable tipo diccionario, ejm diccionario {1:"F",2:"U",3:"E",4:"G",5:"O"}
	for x in clave:
		diccionario[contador]=x
		contador=contador+1
	###variable tipo lista,listaOrdenada guarda la palabra secreta ordenada alfabéticamente,ejem [E,F,G,O,U]
	listaOrdenada=sorted(diccionario.values())	
	#recorre palabra secreta ordenada alfabéticamente y la guarda en variable tipo diccionario, diccionarioOrdenado {1:"E",2:"F",3:"G",4:"O",5:"U"} 
	for x in listaOrdenada:
		diccionarioOrdenado[contadorDos]=x
		contadorDos=contadorDos+1
	#recorre palabra secreta, {1:"F",2:"U",3:"E",4:"G",5:"O"}	
	for c,v in diccionario.items():
	#recorre palabra secreta ordenada alfabéticamente, {1:"E",2:"F",3:"G",4:"O",5:"U"}  
		for cc,vv in diccionarioOrdenado.items():
	#si los valores de las letras son iguales, se guarda la clave de diccionarioOrdenado en la calve de diccionarioClave
	#ejem {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 
			if v==vv:
				diccionarioClave[contadorTres]=cc
				contadorTres=contadorTres+1
				break
	###diccionarioClave guarda la palabra secreta odrenada según el diccionario-diccionarioOrdenado, ejem, {1: 2, 2: 5, 3: 1, 4: 3, 5: 4} 		
	return diccionarioClave