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

"""Dependent on movieSearch function, takes 'who does ACTOR play in FILM' as input and returns their role in the film"""
def roleSearch(receiveMess):
	i = IMDb(accessSystem='http')
	messSplit = receiveMess.split(" in ")
	actorNamePull = str(messSplit[0])
	messSplit = str(messSplit[1])
	actorNamePull = actorNamePull.replace("who ","").replace("does ","").replace(" play","")
	movieID = movieSearch(messSplit) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	castDict = {} #Creates empty dictionary
	cast = movie.get('cast') 
	try: #Pulls all actors out of the film until it fails.
		for actor in cast[:9999]:
			actorName = actor['name']
			actorRole = actor.currentRole
			castDict ["{0}".format(actor['name'])] = "{0}".format(actorRole) #Adds entries to dictionary with actor name as key, role as value. 
	finally:
		return str(castDict[actorNamePull])

"""Dependent on movieSearch function, takes movie title as input and returns castDict, a full dictionary of all cast members, with their role as the value"""
def actorDict(receiveMess):
	i = IMDb(accessSystem='http')
	messSplit = receiveMess.split(" in ")
	actorNamePull = str(messSplit[0])
	messSplit = str(messSplit[1])
	actorNamePull = actorNamePull.replace("who ","").replace("does ","").replace(" play","")
	movieID = movieSearch(messSplit) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID) 
	castDict = {} #Creates empty dictionary
	cast = movie.get('cast') 
	try: #Pulls all actors out of the film until it fails.
		for actor in cast[:9999]:
			actorName = actor['name']
			actorRole = actor.currentRole
			castDict ["{0}".format(actor['name'])] = "{0}".format(actorRole) #Adds entries to dictionary with actor name as key, role as value. 
	finally:
		return str(castDict[actorNamePull])

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

"""Dependent on movieSearch function, takes movie title as input and a number of actors, returns a string with the format 'ACTOR as ROLE'"""
def actorNum(movieTitle, endVar=5):
	castStr = ""
	numCount = 0	
	i = IMDb(accessSystem='http')
	movieID = movieSearch(movieTitle) #Pulls movieID from movieSearch func
	movie = i.get_movie(movieID)  #Pulls actors
	cast = movie.get('cast')
	for actor in cast[0:int(endVar)]:
		if numCount == 0:
			castStr = castStr + "{0} as {1}".format(actor['name'], actor.currentRole)
			numCount = numCount + 1
		else: 
			castStr = castStr + "\n" + "{0} as {1}".format(actor['name'], actor.currentRole)
	return castStr	