#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int (input("Valor de a: "))
b = int (input("Valor de b: "))
u = int (input("Valor de U(0): "))
cantidad = int (input("Cantidad de números a mostar: "))
lista1 = []

sucesion = u
lista1.append(sucesion)
z = 1 #Rellenar lista
x = 1 #Contador
while(x < cantidad):
	sucesion = a * sucesion + b
	lista1[0:z] += [str(sucesion)]
	z += 1
	x += 1

print ("Sucesión: ", lista1)
