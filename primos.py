#!/usr/bin/python3.8

# Calcular numeros primos
#


# Definicion de variables
i=1
divisor=0
primo=True

# Main
while True:
	divisor=i-1
	while divisor > 1: 
		primo=True
		if i%divisor == 0: # si da resto 0 no es primo y rompe bucle
			primo = False
			break
		divisor=divisor-1
	if primo == True: # si termina el bucle es primo
		print (str(i))
	i=i+1 # pasamos al siguiente numero
