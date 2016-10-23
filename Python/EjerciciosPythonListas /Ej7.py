#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenamos lista
posiciones =int (input ("Tamaño de la lista: "))
lista1 = []
i = 0 
while(i < posiciones):
	lista1[0:i] += [str(input("Elemento: "))]
	i += 1

#Imprimimos lista
print("Lista 1: ",lista1)

#Borramos el elemento repetido de la ultima posicion
for x in range(len(lista1)-1,-1,-1):
	if(lista1[x] in lista1[:x]):
		del(lista1[x])

#Imprimimos lista			
print("Lista final: ",lista1)

