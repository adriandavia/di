#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista
numero = int (input("Dime el tamaño de la lista: "))
lista = []
i = 0
while (i < numero):
	#print(lista)
	lista[0:i] += [str(input("Elemento: "))]
	i = i + 1

#Imprimos lista y sustituimos una palabra por otra 
print (lista)
eliminar = input("Sustituir la palabra: ")
sustituto = input("Nueva palabra: ")
num = lista.index(eliminar)
lista[num] = sustituto
print (lista)

