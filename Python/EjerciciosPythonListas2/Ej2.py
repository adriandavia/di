#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = int (input("Numero: "))
lista1 = []

#Calcular los divisores 
i = 1 #Para calcular los divisores
x = 0 #Para rellenar la lista
while (i <= numero):
	if (numero % i == 0):
		lista1[0:x] += [str(i)]
		x += 1
		i += 1 
	else:
		i += 1 

#Imprimimos divisores del numero insertado
print ("Divisores: ", lista1)
