from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()

"""Takes a movie title as input, runs a search and returns the movieID for the first match in the list"""

#Commented out for testing purposes
'''def movieSearch(movieTitle):
	for movie in ia.search_movie(movieTitle):
		results = ia.search_movie(movieTitle)
		first = results[0]
		return first.movieID
		break'''

"""Dependent on movieSearch function, takes movie title as input and returns a list(castList) containing the top 5 cast names"""
def castGet(movieTitle):
	castList = [] #Creates an empty list
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = ia.get_movie(movieID) 
	for i in range(0,5): #Pulls first 5 actors and adds to list
		castPull = movie['cast'][i]
		appendName = castPull['name']
		castList.append(appendName)
	return castList

#Testing
title = input('Input Title ') 
test = movieSearch(title)
print (test)
print (castGet(title))
