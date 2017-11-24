from imdb import IMDb
from MovieID import movieSearch
from castlist import castGet
i = IMDb()

#Testing------------------------------------------------------------------------------------------------#

#seriesTitle = input(" Input a tv series title. ")
#episodeNumber = int(input("Episode number ? "))
#seasonNumber = int(input("Season number ? "))

#-------------------------------------------------------------------------------------------------------

#seriesID = movieSearch(seriesTitle)
#m = i.get_movie(str(seriesID))
#i.update(m, 'episodes') 
#episodes=m['episodes']

#--------------------------------------
def seasonsEpisodesCounter(seriesTitle):  #if kind===tv series
	"""Takes the title as input and returns a tuple of the number of seasons and episodes."""
	seriesID = movieSearch(seriesTitle)
	m = i.get_movie(str(seriesID))
	i.update(m, 'episodes') 
	e=m['episodes']
	

	seasonCount = 0
	episodeCount = 0
	for k,v in e.items():
		seasonCount = seasonCount + 1 #number of seasons

	#message = "The Series " + str(m['title'])+" has " + str(seasonCount) +  " seasons"

	for k,v in e.items():
		for x,y in v.items():
			episodeCount = episodeCount + 1

	#message = message + " and "+ str(episodeCount) + " episodes."
	return (seasonCount, episodeCount)

#Test-----
#seasons,episodes = seasonsEpisodesCounter(seriesTitle)
#print(str(seasons))
#print(str(episodes))
#--------------------------------------




#def listOfEpisodes(episodes):
#	message = ""
#	for k,v in episodes.items():
#		for x,y in v.items():
#			message = message + str(k) + str(x)
#listOfEpisodes(episodes)
#print(seasonsEpisodesCounter(seriesTitle)) #test
def listOfEpisodes(seriesTitle):#if kind===tv series
	"""Takes as input a title and returns an unordered list of seasons and ordered list of episodes as a string"""
	seriesID = movieSearch(seriesTitle)
	m = i.get_movie(str(seriesID))
	i.update(m, 'episodes') 
	episodes=m['episodes'] 
	message =""
	for k,v in episodes.items():#k is the key of the dict--season_number(also a dictionary).#v is the value--#episode_number:movie object)
		message = message + "`season` " + str(k) +"\n"
		for x,y in v.items():#x is the key of the dict--episode-number.#y is the value--movei object
			message = message + " `episode` " + str(x)
			message = message + ": " + y['title']
			message = message + "\n"
	return message
#-------------------------------------------------------------------------------------------------------------
#print (listOfEpisodes(episodes))
#print(listOfEpisodes(seriesTitle))
#--------------------------------------------------------------------------------------------------------------
def infoAboutEpisode(seriesTitle,seasonNumber,episodeNumber):
	"""Takes a string and two numbers as input and returns a string with the title of the episode, the number and the cast, plot and rating."""
	seriesID = movieSearch(seriesTitle)
	m = i.get_movie(str(seriesID))
	i.update(m, 'episodes') 
	e=m['episodes']
	specificEpisode = m['episodes'][seasonNumber][episodeNumber]
	episodeTitle = specificEpisode['title']
	episodeID = movieSearch(episodeTitle)
	episode = i.get_movie(str(episodeID))
	info = ""
	info  = info + "`The main cast for episode` " + str(episodeNumber) + " `from season` " + str(seasonNumber) + " - " + str(specificEpisode['title']) + "`is as follows:` \n"
	info = info + castGet(episodeTitle)   
	plot = episode['plot']	
	info = info + "\n" + "`The plot should be:` \n" + str(plot)		
	rating = episode['rating']
	info = info + "\n " + "`Episode's rating is:` " + str(rating)
	return (info)
#print(infoAboutEpisode(4,2))