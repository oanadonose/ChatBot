from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()

def writerGet(movieTitle):
	"""Takes movie title as input and returns a tuple of the no. of writers and a list containing all writers' names"""
	writerListStr = []
	movieID = movieSearch(movieTitle)
	movie = ia.get_movie(movieID)
	writerList = movie['writer']
	numberOfWriters = len(writerList)
	for i in range(0,numberOfWriters):
		writerPull = movie['writer'][i]
		appendName = writerPull['name']
		writerListStr.append(appendName)
		strWriter = str(writerListStr).replace("[","").replace("]","").replace("'","")
	return (numberOfWriters,strWriter)
print(writerGet("Lucifer"))