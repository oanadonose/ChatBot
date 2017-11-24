from imdb import IMDb
import random

i = IMDb()
def getRating(movie):
	"""Takes a movie title as input and returns the title and IMDB rating"""	
	movieList = i.search_movie(movie)
	firstMatch = movieList[0]
	i.update(firstMatch)
	try:
		return("%s : %s" % (firstMatch['title'], firstMatch['rating']))
	except:
		return(KeyError('Could not find that film!'))

def searchKeyword(receiveMess):
	"""Takes a keyword as input, and searches for films containing that keyword, returning it's title and rating"""
	inputList = receiveMess.split()
	for n in range(0, len(inputList)-1):
		if inputList[n] == "about":
			keyword = inputList[n+1]
			break #selects the keyword as the word after "about" or "involving" in the input (i.e "movies ABOUT zombies")
		else:
			continue
	movieList = i.get_keyword(keyword) #returns a list of movies that contain a given keyword
	x = random.randint(0, 50)
	try:
		film = movieList[x]
	except IndexError:
		return('Could not find any films about that!')
	i.update(film)
	return("I recommend "+ film['title'] + ", with a rating of "+ str(film['rating']))