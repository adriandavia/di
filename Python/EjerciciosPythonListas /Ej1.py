#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista
numero = int (input("Dime el tamaño de la lista: "))
lista = []
i = 0
while (i < numero):
	lista[0:i] += [str(input("Elemento: "))]
	i = i + 1
#Imprimir lista y numero de elementos de la lista
print (lista,"\nNúmero de elementos en la lista",i)	

