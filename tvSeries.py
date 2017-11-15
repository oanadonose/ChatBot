from imdb import IMDb
from MovieID import movieSearch
from castlist import castGet
i = IMDb()

seriesTitle = input(" Input a tv series title. ")

#episodeNumber = int(input("Episode number ? "))
#seasonNumber = int(input("Season number ? "))
seriesID = movieSearch(seriesTitle)
m = i.get_movie(str(seriesID))
i.update(m, 'episodes') 
e=m['episodes']
#--------------------------------------
def seasonsEpisodesCounter(seriesTitle):
	

	seasonCount = 0
	episodeCount = 0
	for k,v in e.items():
		seasonCount = seasonCount + 1 #number of seasons

	message = "The Series " + str(m['title'])+" has " + str(seasonCount) +  " seasons"

	for k,v in e.items():
		for x,y in v.items():
			episodeCount = episodeCount + 1

	message = message + " and "+ str(episodeCount) + " episodes."
	return message

#print(seasonsEpisodesCounter(seriesTitle)) #test
#-------------------------------------------------------------------------------------------------------------

moreInfo = input("Would you like to see more info about a specific episode? y/n ")
if moreInfo=="y":
	seasonNumber = int(input(" Season number ? "))
	episodeNumber = int(input(" Episode number ? "))
	specificEpisode = m['episodes'][seasonNumber][episodeNumber]
	episodeTitle = specificEpisode['title']
	episodeID = movieSearch(episodeTitle)
	episode = i.get_movie(str(episodeID))
	print("The cast from episode " + str(episodeNumber) + " from season " + str(seasonNumber) + " - " + str(specificEpisode['title']) + "is as follows : ")
	print(castGet(episodeTitle))  #everything to be formatted to look nice 
	plot = episode['plot']			
	rating = episode['rating']
	directorList = episode['director']
	writerList = episode['writer']
	producerList = episode['producer']
	print(rating)
	print(plot)
	print("The director(s) are: ")
	for director in directorList:
		print(director['name'])
	print("The writer(s) are: ")
	for writer in writerList:
		print(writer['name'])
	print("The producers are: ")
	for producer in producerList:
		print(producer['name'])