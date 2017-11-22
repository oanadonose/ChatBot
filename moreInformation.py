from imdb import IMDb
from MovieID import movieSearch
from castlistOld import castGet
from kindOfShow import determineKind

i = IMDb()

#Testing----------------------------------------------------------------------------------------------
#title = input (" >  >  >")
#-----------------------------------------------------------------------------------------------------

def moreInfo( title ):
	kind = str(determineKind(title))
	titleID = movieSearch(title)
	m = i.get_movie(str(titleID))  #retrieves the movie object for the title input

	info = "Here is a more detailed description of the " + kind + " that you were looking for: \n" + "\n"
	
	longTitle = m['smart long imdb canonical title']
	info = info + str(longTitle) 
	
	if kind=='tv series' or kind=='movie':
		rating = m['rating']
		info = info  + " " + str(rating) + "\n"
		info = info + "\nThis is the main cast:\n "
		castList = castGet(title)
		cast = ""
		for actor in castList:
			cast = cast  + str(actor) + "\n "
		info = info + cast + "\n"
		plot = m['plot']
		info = info + "This should be the plot:\n" + str(plot) + "\n"
		info = info + "\nThe directors: \n "
		directorList = m['director']
		directors = ""
		for director in directorList:
			directors = directors + str(director) + "\n "
		info = info + directors	
		info = info + "\nThe writers: \n "
		writerList = m['writer']
		writers = ""
		for writer in writerList:
			writers = writers + str(writer) + "\n "
		info = info + writers + "\n"

		info = info + "The producers: \n "
		producerList = m['producer']
		producers = ""
		for producer in producerList:
			producers = producers + str(producer) + "\n "
		info = info + producers
	#-------------------------------------------------------------DONE
	else:
		seriesOfEpisodeInput = m['episode of'] #y returns title of the series the episode belongs to
		#print(seriesOfEpisodeInput) #y
		seriesOfEpisodeID = movieSearch(str(seriesOfEpisodeInput)) # retrieves the series ID
		#print(seriesOfEpisodeID) #y
		seriesOfEpisode = i.get_movie(str(seriesOfEpisodeID)) # from series ID it updates the movie object 'SeriesOfEpisode'
		#print(seriesOfEpisode) #y
		info = ""
		longTitleEpisode = m['title']
		longTitleSeries = seriesOfEpisode['smart long imdb canonical title']
			
		info = info + "The episode that you entered("+ longTitleEpisode + ") belongs to the series " + str(longTitleSeries) + "\n"
		
		seasonOfEpisode = m['season']   
		numberOfEpisode = m['episode']   

		i.update(seriesOfEpisode,'episodes')   

		e = seriesOfEpisode['episodes'][seasonOfEpisode][numberOfEpisode] 

		i.update(e)

		rating = e['rating']
		info = info  + "\nEpisode's rating: " + str(rating)
		info = info + "\nSeries' rating: " + str(seriesOfEpisode['rating']) + "\n"
		info = info + "\nThis is the main cast:\n "
		castList = castGet(title)
		cast = ""
		for actor in castList:
			cast = cast  + str(actor) + "\n "
		info = info + cast + "\n"
		plot = e['plot']
		info = info + "This should be the plot:\n" + str(plot) + "\n"
		info = info + "\nThe directors: \n "
		directorList = e['director']
		directors = ""
		for director in directorList:
			directors = directors + str(director) + "\n "
		info = info + directors	
		info = info + "\nThe writers: \n "
		writerList = m['writer']
		writers = ""
		for writer in writerList:
			writers = writers + str(writer) + "\n "
		info = info + writers

		info = info + "\nThe producers: \n "
		producerList = e['producer']
		producers = ""
		for producer in producerList:
			producers = producers + str(producer) + "\n "
		info = info + producers

	return info



#Testing-------------------------------------------------

#print(moreInfo(title))


#---------------------------------------------------------