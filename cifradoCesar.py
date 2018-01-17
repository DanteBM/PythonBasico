## Cifrado por desplazamiento ##
def cifrar(mensaje, n):# Definicion de la funcion cifrar
	""" Funcion que realiza el cifrado cesar.
	a - z en el intervalo 97 - 122
	A - Z en el intervalo 65 - 90. """
	entrada = list(mensaje) #Se transforma el mensaje en una nueva lista
	salida = [] #Se crea otra lista donde estara el mensaje cifrado

	for letra in entrada: #For para recorrer caracter a caracter el mensaje escrito
		m = ord(letra) #Se obtiene el valor ASCII del caracter en flujo

		if m > 96 and m < 123: #Si el valor es True, significa que el valor ASCII es una letra minuscula
			m += n #Se realiza el desplazamiento del valor ASCII
			if m > 122: #Si es True, significa que se ha pasado de la zeta minuscula
				m %= 122 #Obtenemos el residuo de la division
				m += 96 #Se le agrega el valor minimo de las minusculas

		if m > 64 and m < 91: #Si el valor es True, significa que el valor ASCII es una letra mayuscula
			m += n #Se realiza el desplazamiento del valor ASCII
			if m > 90: #Si es True, significa que el valor se ha pasado de la zeta mayuscula
				m %= 90 #Obtenemos el residuo de la division
				m += 64 #Se le agrega el valor minimo de las mayusculas

		salida.append(chr(m)) #Se agrega elemento a la lista del mensaje cifrado

	print("El mensaje cifrado es:\n"+"".join(salida)) #Se imprime el mensaje cifrado, usando el metodo join para que se vea como cadena
	caracterMasUsado(salida)#Se manda a llamar la funcion caracterMasUsado, y se le pasa el mensaje cifrado

def descifrar(mensaje, n): #Definicion de la funcion descifrar
	""" Funcion que descifra un mensaje con cifrado cesar. """
	entrada = list(mensaje) #Se transforma el mensaje cifrado en una nueva lista
	salida = [] #Se crea otra lista donde estara el mensaje descifrado

	for letra in entrada: #For para recorrer caracter a caracter el mensaje cifrado
		m = ord(letra) #Se obtiene el valor ASCII del caracter en flujo

		if m > 96 and m < 123: #Si el valor es True, significa que el valor ASCII es una letra minuscula
			m -= n #Se realiza el desplazamiento del valor ASCII
			if m < 97: #Si el valor es True, significa que el valor ASCII esta por detras de la a minuscula
				m = 97 - m #Se realiza la diferencia entre la a minuscula y el valor ASCII
				m = 123 - m #Se resta la z minuscula de la diferencia anterior

		if m > 64 and m < 91: #Si el valor es True, significa que es una mayuscula
			m -= n #Se realiza el desplazamiento  "hacia atras"
			if m < 65: #Si el valor es True, significa que esta por detras de la a mayuscula
				m = 65 - m #Se realiza la diferencia entre la a mayuscula y el valor ASCII
				m = 91 - m #Se resta la z mayuscula de la diferencia anterior

		salida.append(chr(m)) #Se agrega elemento a la lista del mensaje descifrado

	print("El mensaje descifrado es:\n"+"".join(salida)) #Se imprime el mensaje cifrado, usando el metodo join para que se vea como cadena
	caracterMasUsado(salida)#Se manda a llamar la funcion caracterMasUsado, y se le pasa el mensaje descifrado

def caracterMasUsado(mensaje):#Definicion de la funcion caracterMasUsado
	""" Funcion que imprime en pantalla una lista con el o los caracteres mas usados del mensaje, 
	ya sea cifrado o descifrado segun en donde sea llamada dicha funcion. """
	letrasUsadas = list(set(mensaje))#Se transforma el mensaje en un conjunto para eliminar elementos duplicados, posteriormente se transforma en una lista para que la estructura de datos tenga orden
	diccionario = dict(zip(letrasUsadas,[1]*len(letrasUsadas)))#Se crea un diccionario donde las claves son las letras que tiene el mensaje, y se inicializan sus valores con 1
	mensajeL = list(mensaje)#Se crea otra lista donde este el mensaje original
	for i in letrasUsadas:#for que recorre la lista que contiene las letras existentes en el mensaje
		diccionario[i] = mensajeL.count(i)#Se actualiza los valores de las claves del diccionario

	numMax = max(diccionario.values())#Se haya el numero mas grande entre los valores del diccionario
	caracteresMasUsados = []#Se crea una nueva lista vacia
	for i in letrasUsadas:#Se vuelve a usar for para recorrer nuevamente las letras existentes
		if diccionario[i] == numMax:#Si el valor de la clave en flujo es igual al maximo, se ejecuta la siguiente linea
			caracteresMasUsados.append(i)#Se agrega la letra en flujo a la lista de caracteres mas usados

	print("Caracter(es) mas usado(s):\n"+str(caracteresMasUsados)+"\n\n")

while True: #Condicion para que el programa se ejecute continuamente
	print("Menu") #Se imprime menu
	print("1.- Codificar mensaje") #Se imprimen las opciones
	print("2.- Descifrar mensaje") #Se imprimen las opciones
	print("3.- Salir") #Se imprimen las opciones
	op = input("Eliga una opcion: ") #Se le pregunta al usuario por la opcion

	if op == "1": #Segmento del codigo que se ejecuta si el usuario eligio cifrar
		numero = int(input("Ingresa el numero de desplazamiento: ")) #Se le pide al usuario por la clave de cifrado Cesar
		if numero > 0: #Se comprueba que el numero de desplazamiento sea mayor a cero
			cadena = input("Ingresa el texto a cifrar: ") #Se le pide al usuario por la cadena a cifrar
			cifrar(cadena, numero) #Se manda a llamar la funcion cifrar y se le pasa los parametros anteriores
		else:#Segmento del codigo si el numero de desplazamiento es menor que cero
			print("El numero de desplazamiento debe ser mayor que cero\n\n") #Se le indica al usuario que debe ingresar un numero mayor a cero

	elif op == "2": #Segmento del codigo que se ejecuta si el usuario eligio descifrar
		numero = int(input("Ingresa el numero de desplazamiento: ")) #Se le pide al usuario la clave con la cual se realizo el cifrado Cesar
		if numero > 0: #Se comprueba que el numero de desplazamiento sea mayor a cero
			cadena = input("Ingresa el texto a descifrar: ") #Se le pide al usuario por la cadena cifrada
			descifrar(cadena, numero) #Se manda a llamar la funcion descifrar y se le pasa los parametros anteriores
		else:#Segmento del codigo si el numero de desplazamiento es menor que cero
			print("El numero de desplazamiento debe ser mayor que cero\n\n") #Se le indica al usuario que debe ingresar un numero mayor a cero			

	elif op == "3": #Segmento del codigo si el usuario desea salir
		print("Fin del programa\n") #Se imprime que es el final del programa
		print("Programa realizado por Dante Bermudez Marban\n") #Nombre del autor del codigo
		break #Palabra reservada para salir del ciclo while. Es la unica manera de salir del programa

	else: #Segmento del codigo si el usuario tecleo otra cosa
		print("Opcion no valida\n\n") #Se le indica al usuario que lo que ingreso no es valido