from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()
		
'''Takes a dictionary as input, converts all the keys to lowercase and places them as new keys, with the original as the value'''
def dictConv(dictInput):
	lowerDict = {} #Empty dict
	for key in dictInput: #iterates over all keys
		lowerDict [key.lower()] = key #Fills the new dictionary
	return lowerDict


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


"""Dependent on movieSearch function, takes movie title as input and returns a list(castList) containing a variable number of cast names"""
def castGetMulti(movieTitle, endVar=5):
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
def actorDict(receiveMess):
	i = IMDb(accessSystem='http')
	movieID = movieSearch(receiveMess) #Pulls movieID from movieSearch func
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


"""Dependent on movieSearch function, takes 'who does ACTOR play in FILM' as input and returns their role in the film or which actor plays ROLE in FILM and returns the actor"""
def roleSearch(receiveMess):
	i = IMDb(accessSystem='http')
	if "does" not in receiveMess:
		try:
			messSplit = receiveMess.lower().split(" in ")
			charPull = str(messSplit[0])
			filmPull = str(messSplit[1]).replace("?","").replace("!","").replace(".","").replace(",","")
			charPull = charPull.replace("which ","").replace("actor ","").replace("plays ","").replace("who ","").replace(", ","")
			roleDictPull = roleDict(filmPull) #Gets the dictionary from film name
			lowerDict = dictConv(roleDictPull) #Creates a dictionary of lowercase roles against their original versions
			upperChar = lowerDict[charPull] #Pulls the original version from the lowercase user input
			return (str(charPull).title() + " is played by " + (str(roleDictPull[upperChar])) + " in " + str(filmPull).title())
		except KeyError:
			return("That character is not in that film")
	else:
		try: 
			messSplit = receiveMess.lower().split(" in ")
			actorPull = str(messSplit[0])
			filmPull = str(messSplit[1]).replace("?","").replace("!","").replace(".","").replace(", ","")
			actorPull = actorPull.replace("who ","").replace("does ","").replace(" play","").replace("which ","").replace("character ","").replace("charecter","").replace("charctor","")
			actorDictPull = actorDict(filmPull) #Gets the dictionary from film name
			lowerDict = dictConv(actorDictPull) #Creates a dictionary of lowercase actors against their original names
			upperActor = lowerDict[actorPull] #Pulls the original version from the lowercase user input
			return (upperActor + " plays " + str(actorDictPull[upperActor] + " in " + str(filmPull).title()))
			#actorDictPull = actorDict(filmPull)
			#return str(actorDictPull[actorPull])
		except KeyError:
			return("That actor is not in that film")
