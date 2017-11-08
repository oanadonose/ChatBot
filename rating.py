from imdb import IMDb

i = IMDb()
def getRating():
	"""Asks the user for a movie title as input and returns the title and IMDB rating"""
	movie = raw_input("Enter a movie title: ")
	movieList = i.search_movie(movie)
	firstMatch = movieList[0]
	i.update(firstMatch)
	return "%s : %s" % (firstMatch['title'], firstMatch['rating'])

#print getRating()

def moreFilms():
	"""Takes user input and recommends a film with a similar or higher rating"""
	rating = raw_input("Enter a rating: ")
	movieList = i.search_movie()
	print movieList

print moreFilms()