#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista
numero = int (input("Dime el tamaño de la lista: "))
lista = []
i = 0
while (i < numero):
	lista[0:i] += [str(input("Elemento: "))]
	i = i + 1
#Imprimimos lista y buscamos una palabra
print (lista)
palabras = input("Dime la palabra a buscar: ")
print ("La palabra buscada aparece ",lista.count(palabras)," veces en la lista.") 	

