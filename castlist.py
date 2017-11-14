from imdb import IMDb
from MovieID import movieSearch
i = IMDb()

"""Dependent on movieSearch function, takes movie title as input and returns a list(castList) containing the top 5 cast names"""
def castGet(movieTitle):
	castList = [] #Creates an empty list
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	for i in range(0,5): #Pulls first 5 actors and adds to list
		castPull = movie['cast'][i]
		appendName = castPull['name']
		castList.append(appendName)
	return castList
