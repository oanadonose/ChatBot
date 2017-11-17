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
		#castList = [x.encode('utf-8') for x in castList]
		strCast = str(castList).replace("[","").replace("]","").replace("'","")
	return strCast

"""Dependent on movieSearch function, takes movie title as input and returns castDict, a full dictionary of all cast members, with their role as the value"""
def actorDict(movieTitle):
	i = IMDb(accessSystem='http')
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	castDict = {} #Creates empty dictionary
	cast = movie.get('cast') 
	try: #Pulls all actors out of the film until it fails.
		for actor in cast[:9999]:
			actorName = actor['name']
			actorRole = actor.currentRole
			castDict ["{0}".format(actor['name'])] = "{0}".format(actorRole) #Adds entries to dictionary with actor name as key, role as value. 
	finally:
		return castDict

"""Dependent on movieSearch function, takes movie title as input and returns roleDict, a full dictionary of all roles, with their actor as the value"""
def roleDict(movieTitle):
	i = IMDb(accessSystem='http')
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	roleDict = {} #Creates empty dictionary
	cast = movie.get('cast') 
	try: #Pulls all actors out of the film until it fails.
		for actor in cast[:9999]:
			actorName = actor['name']
			actorRole = actor.currentRole
			roleDict ["{0}".format(actorRole)] = "{0}".format(actor['name']) #Adds entries to dictionary with actor name as key, role as value. 
	finally:
		return roleDict	

"""Dependent on movieSearch function, takes movie title as input and returns actorNumDict, a full dictionary of a specified number of cast members, with their role as the value"""
def actorNumDict(movieTitle, endVar=5):
	i = IMDb(accessSystem='http')
	castList = [] #Creates an empty list
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	for i in range(0,int(endVar)): #Pulls first 5 actors and adds to list
		actorNumDict = {}
		cast = movie.get('cast')
		try:
			for actor in cast[:int(endVar)]:
				actorName = actor['name']
				actorRole = actor.currentRole
				actorNumDict ["{0}".format(actor['name'])] = "{0}".format(actorRole)
		finally:
			return actorNumDict

