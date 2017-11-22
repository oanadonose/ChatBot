from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()

def directorGet(movieTitle):
	"""Takes movie title as input and returns a tuple of the no. of directors and a list containing all directors' names"""
	directorListStr = []
	movieID = movieSearch(movieTitle)
	movie = ia.get_movie(movieID)
	directorList = movie['director']
	numberOfDirectors = len(directorList)
	for i in range(0,numberOfDirectors):
		directorPull = movie['director'][i]
		appendName = directorPull['name']
		directorListStr.append(appendName)
		strDirector = str(directorListStr).replace("[","").replace("]","").replace("'","")
	return (numberOfDirectors,strDirector)
print(directorGet("Lucifer"))