char = input ()
def isVowel(char):
	if char in "aeiouAEIOU":
		return True
	else: 
		return False

print (isVowel(char))