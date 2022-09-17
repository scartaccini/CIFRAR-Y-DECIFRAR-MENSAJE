def ingresoMensaje(clave):	
	while (True):
		mensaje=input("Ingrese mensaje para ser codificado").upper()
		if (len(mensaje) >= 16 and len(mensaje) <= 60):
			mensaje=mensaje.split()
			mensaje="".join(mensaje)
			if (mensaje.isalpha()):
				while len(mensaje) % len(clave) != 0 :
					mensaje = mensaje + "@"
				print("Mensaje ingresado! ")
				return mensaje	
			else:
				print("El mensaje solo puede tener letras(A-Z)")
		else:
			print("El mensaje tiene que tener más de 15 caractéres y menos de 61")				
### guarda el texto a cifrar en variable mensaje de tipo String,sin espacios,solo letras
### el tamaño del mensaje tiene que ser divisible entrre el tamaño de la palabra secreta,si no, se rellena con @
### ejm, HOLAQUETALCOMOESTAS % FUEGO --->>> 19/5 --->>>   HOLAQUETALCOMOESTAS@