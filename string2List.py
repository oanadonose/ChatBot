#receiveMess = input("***")

def stringToList(receiveMess):
	"""Function that separates the words in the string input and removes ?.,!, returning a list of all the words"""
	receiveMess = receiveMess.split()
	for word in receiveMess:
		for character in word:
			wordPlace = receiveMess.index(word)
			if character=="?" or character=="." or character=="," or character=="!":
				wordGood = word.replace(character,"")
				receiveMess[wordPlace] = wordGood
	return receiveMess
