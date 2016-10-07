#!/usr/bin/env python

#EJERCICIO PARA CONTAR CUANTOS ELEMENTOS DE CADA HAN PEDIDO 
def item_order (cadena): 
	#QUANTITY OF EACH ITEM
	ensalada = cadena.count("ensalada") 
	hamburguesa = cadena.count("hamburguesa")
	agua = cadena.count("agua")
	#PRINT CHAIN 
	print("Ensalada: ", ensalada, "Hamburguesa: ", hamburguesa, "Agua: ", agua)

pedido = input("Pedido realizado: ") #INSERT CHAIN ​​WITH ORDER

item_order(pedido) #CALL FUCTION
