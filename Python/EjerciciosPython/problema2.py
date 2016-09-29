char = input ()

def isVowel (char):
	if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U":
		return True
	else:
		return False

print (isVowel(char))