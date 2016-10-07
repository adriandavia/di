#!/usr/bin/env python

#EJERCICIO PARA CALCULAR EL EXPONENCIAL

def iterPower (base, exp): #CALCULATING FUCTION
	mult = base 
	while exp > 1:
		base = base * mult
		exp = exp - 1
	return base

base = int(input("Base: ")) #INSERT BASE 
exp = int(input("Exponente: ")) #INSERT EXPONENT
print (iterPower(base, exp)) #ROLE CALL AND PRINT

