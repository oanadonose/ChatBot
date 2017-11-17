from imdb import IMDb
from MovieID import movieSearch


"""Dependent on movieSearch function, takes movie title as input and returns a list(castList) containing the top 5 cast names"""
def castGet(movieTitle, endVar=5):
	i = IMDb(accessSystem='http')
	castList = [] #Creates an empty list
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	for i in range(0,endVar): #Pulls first 5 actors and adds to list
		castPull = movie['cast'][i]
		
		appendName = castPull['name']
		castList.append(appendName)
		castList = [x.encode('utf-8') for x in castList]
		strCast = str(castList).replace("[","").replace("]","").replace("'","")
	return strCast

