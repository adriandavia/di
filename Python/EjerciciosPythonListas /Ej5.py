#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista
num1 = int (input("Dime el tamaño de la lista 1: "))
lista1 = []
i = 0
while (i < num1):
	lista1[0:i] += [str(input("Elemento: "))]
	i = i + 1

#Rellenar lista
num2 = int (input("Dime el tamaño de la lista 2: "))
lista2 = []
j = 0
while (j < num2):
	lista2[0:j] += [str(input("Elemento: "))]
	j = j + 1

#Recorremos la lista para borrar en la lista1 los elementos en comun
#en las dos listas
if (len(lista1) > len(lista2)):
	for x in range(len(lista1)-1,-1,-1):
		for a in range (len(lista2)-1,-1,-1):
			if (lista1[x] == lista2[a]):
				lista1.remove(lista2[a])
else:
	for x in range(len(lista2)-1,-1,-1):
		for a in range (len(lista1)-1,-1,-1):
			if (lista2[x] == lista1[a]):
				lista1.remove(lista2[x])

#Imprimimos la lista con los cambios efectuados 
print ("Lista final: ", lista1)

