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


#wordsList = (stringToList(receiveMess))

#def YEAR(wordsList):
#	for word in wordsList:
#		if word.isdigit():
#			word = int(word)
#			if word>1800 and word<2100:
#				year = word
#			#else:
#				#print("This is not a year we support = > " + str(word))
#	return year
#
#print(YEAR(wordsList))

