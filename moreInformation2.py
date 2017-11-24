from imdb import IMDb
from MovieID import movieSearch
from castlist import castGet
from kindOfShow import determineKind
from directorfunc import directorGet
from writerfunc import writerGet
from producerfunc import producerGet

i = IMDb()

#Testing----------------------------------------------------------------------------------------------
#title = input (" >  >  >")
#-----------------------------------------------------------------------------------------------------

def moreInfo( title ):
	"""Function that retrieves the kind of show, title, year, rating, cast, directors, writers, producers-takes as input a title and returns a string"""
	kind = str(determineKind(title))
	titleID = movieSearch(title)
	m = i.get_movie(str(titleID))  #retrieves the movie object for the title input

	info = "Here is a more detailed description of the " + kind + " that you were looking for: \n" + "\n"
	
	longTitle = m['smart long imdb canonical title']
	info = info + str(longTitle) 
	
	if kind=='tv series' or kind=='movie':
		try:
			#RATING
			rating = m['rating']
			info = info  + " " + str(rating) + "\n"
			#CAST
			info = info + "\n`This is the main cast:`\n "
			castList = castGet(title)
			info = info + castList + "\n"
			#PLOT
			plot = m['plot']
			for plots in plot:
				plotStr = str(plots) + "\n"
			info = info + "\n`This should be the plot:`\n" + plotStr
			#DIRECTORS
			numberOfDirectors,directorList = directorGet(m)
			info = info + "\n" +str(numberOfDirectors) +  " `directors:` \n "
			info = info + str(directorList) + "\n"
			#WRITERS
			numberOfWriters,writerList = writerGet(m)
			info = info + "\n" + str(numberOfWriters) + " `writers:` \n "
			info = info + str(writerList) + "\n"
			#PRODUCERS
			numberOfProducers,producerList = producerGet(m)
			info = info + "\n" + str(numberOfProducers) + " `producers:` \n "
			info = info + str(producerList) + "\n"
		except KeyError:
			info = info + "Sorry, I couldn't handle anything more than that."

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

		info = info + "It is episode " + str(numberOfEpisode) + " from season " + str(seasonOfEpisode) + ".\n"

		e = seriesOfEpisode['episodes'][seasonOfEpisode][numberOfEpisode] 

		i.update(e)
		try:
			rating = e['rating']
			info = info  + "\n`Episode's rating:` " + str(rating)
			info = info + "\n`Series' rating:` " + str(seriesOfEpisode['rating']) + "\n"
			#cast
			info = info + "\n`This is the main cast:`\n "
			castList = castGet(title)
			info = info + castList+ "\n"
			#plot
			plot = e['plot']
			info = info + "`This should be the plot:`\n" + str(plot) + "\n"
			#DIRECTORS
			numberOfDirectors,directorList = directorGet(seriesOfEpisode)
			info = info + "\n`The` " +str(numberOfDirectors) +  " `directors:` \n "
			info = info + str(directorList) + "\n"
			#WRITERS
			numberOfWriters,writerList = writerGet(seriesOfEpisode)
			info = info + "\n`The` " + str(numberOfWriters) + " `writers:` \n "
			info = info + str(writerList) + "\n"
			#PRODUCERS
			numberOfProducers,producerList = producerGet(seriesOfEpisode )
			info = info + "`The` " + str(numberOfProducers) + " `producers:` \n "
			info = info + str(producerList) + "\n"
		except KeyError:
			info = info + "\nSorry, I couldn't handle anything more than that."	
	return info

#Testing-------------------------------------------------

#print(moreInfo("Chloe Does Lucifer"))
#print(moreInfo("The Red Wedding")) #error triggering


#---------------------------------------------------------