varA = 11
varB = 11

if type (varA) == int and type (varB) == int:
	if varA < varB:
		print ("Mas pequeño")
	elif varA == varB:
		print ("Igual")
	else:
		print ("Grande")

if type (varA) == str or type (varB) == str:
	print ("Cadena involucrada")
