#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista
posiciones =int (input ("Tamaño de la lista: "))
lista1 = []
i = 0 
while(i < posiciones):
	lista1[0:i] += [str(input("Elemento: "))]
	i += 1

print ("Lista 1: ", lista1)
#Rellenar lista con los datos de la primera 
#pero de forma inversa
lista2 = []
j = 0 
while(j < posiciones):
	for x in range(len(lista1)-1,-1,-1):
		lista2[0:j] += [str(lista1[x])]
		j += 1	

#Imprimimos la lista numero dos 
print ("Lista 2: ", lista2)
