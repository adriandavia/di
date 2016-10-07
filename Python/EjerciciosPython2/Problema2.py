#!/usr/bin/env python

#EJERCICIO PARA CALCULAR EL MAXIMO COMUN DIVISOR
def gcdIter(a, b): #CALCULATING FUCTION
	resto = 0
	while (b > 0):
		resto = b
		b = a % b
		a = resto 
	return a

a = int(input("Primer valor: ")) #INSERT NUMBER A
b = int(input("Segundo valor: ")) #INSERT NUMBER B

print ("Maximo comun divisor entre ", a, " y ", b, " es : ", gcdIter(a, b))#ROLE CALL AND PRINT
