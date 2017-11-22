from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()

def producerGet(movieTitle):
	"""Takes movie title as input and returns a tuple of the no. of producers and a list containing all producers' names"""
	producerListStr = []
	movieID = movieSearch(movieTitle)
	movie = ia.get_movie(movieID)
	producerList = movie['producer']
	numberOfproducers = len(producerList)
	for i in range(0,numberOfproducers):
		producerPull = movie['producer'][i]
		appendName = producerPull['name']
		producerListStr.append(appendName)
		strproducer = str(producerListStr).replace("[","").replace("]","").replace("'","")
	return (numberOfproducers,strproducer)
print(producerGet("Lucifer"))