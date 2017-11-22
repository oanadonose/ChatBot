from imdb import IMDb

i = IMDb()
def getRating(movie):
	"""Asks the user for a movie title as input and returns the title and IMDB rating"""
	movieList = i.search_movie(movie)
	firstMatch = movieList[0]
	i.update(firstMatch)
	return "%s : %s" % (firstMatch['title'], firstMatch['rating'])

def searchKeyword(keyword):
	"""Takes a keyword as input, and searches for films containing that keyword, returning their title and rating"""
	movieList = i.get_keyword(keyword)
	while True:
		x=0
		film = movieList[x]
		print("I recommend "+ film['title']+", with a rating of "+ film['rating'])
		user = input("Would you like another recommendation? y/n")
		if user == "y":
			x = x+1
		else:
			break
#the get_keyword function appears to be returning an empty list, so for the time being searchKeyword is unfinished