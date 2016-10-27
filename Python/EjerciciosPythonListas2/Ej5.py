#!/usr/bin/env python
# -*- coding: utf-8 -*-

u = int (input("Valor de U(0): "))
cantidad = int (input("Términos a mostrar: "))
sucesion = []

sucesiones = u #U(0)
sucesion.append(u) #Añadimos el primer valor
i = 1 #Bucle 
x = 1 #Añadir
while (i < cantidad): 
	if (sucesiones % 2 == 0 ): #Comrpobamos si la sucesion es par
		sucesiones = int (sucesiones / 2)
		sucesion[0:x] += [str(sucesiones)]
		x += 1
	else: #Comprobamos si la sucesion es impar
		sucesiones = int (3 * sucesiones + 1)
		sucesion[0:x] += [str(sucesiones)] 
		x += 1
	i += 1

#Imprimimos la lista de la solucion
print ("Sucesión:", sucesion)
