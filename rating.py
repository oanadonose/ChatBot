from imdb import IMDb
import random

i = IMDb()
def getRating(movie):
	"""Takes a movie title as input and returns the title and IMDB rating"""	
	movieList = i.search_movie(movie)
	firstMatch = movieList[0]
	i.update(firstMatch)
	return("%s : %s" % (firstMatch['title'], firstMatch['rating']))

def searchKeyword(receiveMess):
	"""Takes a keyword as input, and searches for films containing that keyword, returning their title and rating"""
	inputList = receiveMess.split()
	for n in range(0, len(inputList)-1):
		if inputList[n] == "about":
			keyword = inputList[n+1]
			break #selects the keyword as the word after "about" or "involving" in the input (i.e "movies ABOUT zombies")
		else:
			continue
	movieList = i.get_keyword(keyword) #returns a list of movies that contain a given keyword
	x = 0
	yesResponses = ["yes", "yeah", "okay", "y"]
	noResponses = ["no", "nope", "no thanks", "nah", "n"]
	while True:
		film = movieList[x]
		i.update(film)
		print("I recommend "+ film['title'] + ", with a rating of "+ str(film['rating']))
		user = input("Would you like another recommendation? ")
		if user.lower() in yesResponses: #loop iterates again, this time printing the next movie in movieList
			x = x+1
		elif user.lower() in noResponses:
			break
		else:
			print("I'm afraid I don't understand") #Breaks the while loop in the event of an unexpected input
			break

#print(getRating("avatar"))
searchKeyword('find me a film about cars')