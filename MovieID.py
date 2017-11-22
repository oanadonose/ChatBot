from imdb import IMDb
i = IMDb()

"""Takes a movie title as input, runs a search and returns the movieID for the first match in the list"""
def movieSearch(movieTitle):
	for movie in i.search_movie(movieTitle):
		results = i.search_movie(movieTitle)
		first = results[0]
		return first.movieID
		break 
#Testing
#title = raw_input('Input Title ') 
#test = movieSearch(title)

