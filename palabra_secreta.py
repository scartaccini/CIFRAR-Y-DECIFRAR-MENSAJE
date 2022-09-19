from getpass import getpass

def ingresoSecreto():	
	while (True):
		claveIngresada=getpass("Ingrese una palabra secreta (entre 4 y 8 letras, sin repetirlas) ").upper()
		if (claveIngresada.isalpha()):
			if (len(claveIngresada) >= 4 and len(claveIngresada) <= 8):
				if len(set(claveIngresada))==len(claveIngresada):
					print("Palabra secreta ingresada correctamente! ")
					return claveIngresada
				else:
					print("La palabra secreta no puede tener letras repetidas")
			else:
				print("La palabra secreta tiene que tener más de 3 letras y menos de 9")		
		else:
			print("La palabra secreta solo puede tener letras(A-Z)")
### guarda la palabra secreta-letras sin repetirse- en variable tipo String claveIngresada, ejm FUEGO
#getpass,se usa para no mostrar lo que se ingresa