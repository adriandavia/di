#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = int (input("Numero: "))
lista1 = []

y = 0 #Para rellenar lista 
for a in range(numero+1):
	x = 0 #contador
	i = 1 #calcular divisores
	while (i <= a):
		if (a % i == 0):
			x += 1
			i += 1 
		else:
			i += 1 
	if (a != 0):
		if (x <= 2):
			lista1[0:y] += [str(a)]
			y += 1

#imrpimimos los primos
print ("Numeros primos desde 0 hasta el", numero, ":",lista1)
