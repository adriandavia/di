#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Rellenar lista1
num1 = int(input("Dime el tamaño de la lista: "))
lista1 = []
i = 0
while(i < num1):
	lista1[0:i] += [str(input())]
	i = i + 1
print ("-------------------------------------------------------")
print("Primera lista: ",lista1)

#Rellenar lista2
print ("-------------------------------------------------------")
num2 = int(input("Dime el tamaño de la segunda lista: "))
lista2 = []
j = 0
while (j < num2):
	lista2[0:j] += [str(input())]
	j = j + 1
print ("-------------------------------------------------------")
print("Segunda lista: ",lista2)

#Lista concatenada de list1 y lista2
lista3 = lista1 + lista2
print ("-------------------------------------------------------")
print("Lista conjunta: ",lista3)

#Lista que aparezcan en la primera pero no en la segunda 
lista4 = []
for i in lista1:
	if i not in lista2:
		lista4 = [i] + lista4
print ("-------------------------------------------------------")
print("Lista de palabras que solo aparecen en lista1: ",lista4)

#Lista que aparezcan en la segunda pero no en la primera 
lista5 = []
for i in lista2:
	if i not in lista1:
		lista5 = [i] + lista5
print ("-------------------------------------------------------")
print ("Lista de palabras que solo aparecen en lista2: ", lista5)

#Palabras que aparecen en ambas listas
lista6 = []
for i in lista1:
	if i in lista2:
		lista6 = [i] + lista6
print ("-------------------------------------------------------")
print("Lista de palabras repetidas: ",lista6)
