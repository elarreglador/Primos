#!/usr/bin/python3.8

# Calcular numeros primos
#



i=1
divisor=0
primo=True

while True:
	divisor=i-1
	while divisor > 1:
		primo=True
		if i%divisor == 0:
			primo = False
			break
		divisor=divisor-1
	if primo == True:
		print (str(i))
	i=i+1
