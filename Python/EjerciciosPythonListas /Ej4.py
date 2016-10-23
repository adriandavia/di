#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista
num1 = int (input("Dime el tamaño de la lista: "))
lista1 = []
i = 0
while (i < num1):
	lista1[0:i] += [str(input("Elemento: "))]
	i = i + 1

#Listamos y eliminamos la palabra deseada
print ("Lista 1: ", lista1)
eliminar = input("Borrar la palabra: ")
num = lista1.index(eliminar)
lista1.pop(num)
print ("Lista final: ", lista1)
