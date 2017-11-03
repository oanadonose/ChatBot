from imdb import IMDb
ia = IMDb()

#the_matrix = ia.search_movie("The Matrix")
#first = the_matrix[0]
#test = ia.get_imdbMovieID('The Matrix')
#print test

"""Takes a movie title as input, runs a search and returns the movieID for the first match in the list"""
def movieSearch(movieTitle):
	for movie in ia.search_movie(movieTitle):
		results = ia.search_movie(movieTitle)
		first = results[0]
		return first.movieID
		break 

title = raw_input('Input Title ')
test = movieSearch(title)
print test
