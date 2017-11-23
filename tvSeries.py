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

#def listOfEpisodes(episodes):
#	message = ""
#	for k,v in episodes.items():
#		for x,y in v.items():
#			message = message + str(k) + str(x)
#listOfEpisodes(episodes)
#print(seasonsEpisodesCounter(seriesTitle)) #test
def listOfEpisodes(seriesTitle):#if kind===tv series
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
	seriesID = movieSearch(seriesTitle)
	m = i.get_movie(str(seriesID))
	i.update(m, 'episodes') 
	e=m['episodes']
	specificEpisode = m['episodes'][seasonNumber][episodeNumber]
	episodeTitle = specificEpisode['title']
	episodeID = movieSearch(episodeTitle)
	episode = i.get_movie(str(episodeID))
	info = ""
	info  = info + "The main cast for episode " + str(episodeNumber) + " from season " + str(seasonNumber) + " - " + str(specificEpisode['title']) + "is as follows : \n"
	info = info + castGet(episodeTitle)   
	plot = episode['plot']	
	info = info + "\n" + "The plot should be : \n" + str(plot)		
	rating = episode['rating']
	info = info + "\n " + "Episode's rating is : " + str(rating)
	#directorList = episode['director']
	#writerList = episode['writer']
	#producerList = episode['producer']
	#print(rating)
	#print(plot)
	#print("The director(s) are: ")
	#for director in directorList:
	#	print(director['name'])
	#print("The writer(s) are: ")
	#for writer in writerList:
	#	print(writer['name'])
	#print("The producers are: ")
	#for producer in producerList:
	#	print(producer['name'])
	return (info)
#print(infoAboutEpisode(4,2))