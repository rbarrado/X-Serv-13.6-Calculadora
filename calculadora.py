#!/usr/bin/python

import sys
print(sys.argv)

if len(sys.argv) != 4:
	sys.exit("Numero de argumentos invalido, introduce 3 argumentos: operacion, operando1, operando2")
	
operacion = sys.argv[1]
arg1 = sys.argv[2]
arg2 = sys.argv[3]


if operacion == 'suma':
	resultado = float(arg1) + float(arg2)
	print(str(arg1) + " + " + str(arg2) + " = " + str(resultado))
elif operacion == 'resta':
	resultado = float(arg1) - float(arg2)
	print(str(arg1) + " - " + str(arg2) + " = " + str(resultado))
elif operacion == 'mult':
	resultado = float(arg1) * float(arg2)
	print(str(arg1) + " * " + str(arg2) + " = " + str(resultado))	
elif operacion == 'dividir':
	try:
		resultado = float(arg1) / float(arg2)
		print(str(arg1) + " / " + str(arg2) + " = " + str(resultado))
	except ZeroDivisionError:
		print("Division entre cero, no es posible")
else:
	print("Operacion ivalida, operaciones posibles: suma, resta, mult, dividir")
		
				
