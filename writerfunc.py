from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()

#movieTitle = input("input title : ")

#movieID = movieSearch(movieTitle)
#movie = ia.get_movie(movieID)

def writerGet(movie):
	"""Takes movie OBJECT as input and returns a tuple of the no. of writers and a list containing all writers' names"""
	writerListStr = []
	writerList = movie['writer']
	numberOfWriters = len(writerList)
	for i in range(0,numberOfWriters):
		writerPull = movie['writer'][i]
		appendName = writerPull['name']
		writerListStr.append(appendName)
		strWriter = str(writerListStr).replace("[","").replace("]","").replace("'","")
	return (numberOfWriters,strWriter)
#print(writerGet("Lucifer"))