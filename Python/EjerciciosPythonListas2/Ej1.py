#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenamos lista
posiciones = int (input("Tamaño de la lista: "))
lista1 = []
i = 1
while (i <= posiciones):
	lista1[0:i] += [str(input("Elemento: "))]
	i += 1

#Imprimimos lista original
print ("Lista sin ordenar: ", lista1)

#Ordenamos lista e imprimimos 
lista1.sort()
print ("Lista ordenada alfabeticamente: ", lista1)
