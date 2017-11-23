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
	x = random.randint(0, 50)
	film = movieList[x]
	i.update(film)
	return("I recommend "+ film['title'] + ", with a rating of "+ str(film['rating']))