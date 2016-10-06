#!/usr/bin/env python
def gcdIter(a, b):
	if b == 0:
		return a;
	else:
		gcdIter(b, a%b)

a = int(input("Primer valor: "))
b = int(input("Segundo valor: "))

print (gcdIter(a, b))