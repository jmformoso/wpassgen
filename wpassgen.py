# -*- coding: utf-8
# v0.1.4
# by jtmeros

import sys, os, string, random

caracteres = string.ascii_letters + string.digits + '!@#$%+&*()' # string que incluye letras, números y caracteres especiales
random.seed = (os.urandom(1024))

if len(sys.argv) >= 2:

	try: # si no se introduce un número en el segundo argumento
		longitud = int(sys.argv[1]) # longitud elegida por el usuario
	except:
		longitud = 10 # longitud por defecto


	if len(sys.argv) >= 3:
		if (str(sys.argv[2]) == "-l"):
			caracteres = string.ascii_letters # solo letras

		if (str(sys.argv[2]) == "-ll"):
			caracteres = string.ascii_lowercase #solo letras minúsculas

		if (str(sys.argv[2]) == "-lL"):
			caracteres = string.ascii_uppercase #solo letras mayúsculas

		if (str(sys.argv[2]) == "-n"):
			caracteres = string.digits # solo números

		if (str(sys.argv[2]) == "-s"):
			caracteres = '!@#$%+&*-' # solo símbolos

		if (str(sys.argv[2]) == "-p"):
			caracteres = string.punctuation # solo signos puntuación

		if (str(sys.argv[2]) == "-h"):
			caracteres = string.hexdigits # hexadecimal

		if (str(sys.argv[2]) == "-nl"):
			caracteres = string.digits + string.ascii_letters # letras y números

		if (str(sys.argv[2]) == "-ns"):
			caracteres = string.digits + '!@#$%+&*-' # números y símbolos

else:
	longitud = 10 # longitud por defecto
	

print ''.join(random.choice(caracteres) for i in range(longitud)) # muestra la contraseña