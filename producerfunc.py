from imdb import IMDb
from MovieID import movieSearch
ia = IMDb()

#movieTitle = input("input title : ")

#movieID = movieSearch(movieTitle)
#movie = ia.get_movie(movieID)

def producerGet(movie):
	"""Takes movie OBJECT as input and returns a tuple of the no. of producers and a list containing all producers' names"""
	producerListStr = []
	producerList = movie['producer']
	numberOfproducers = len(producerList)
	for i in range(0,numberOfproducers):
		producerPull = movie['producer'][i]
		appendName = producerPull['name']
		producerListStr.append(appendName)
		strproducer = str(producerListStr).replace("[","").replace("]","").replace("'","")
	return (numberOfproducers,strproducer)
#print(producerGet("Lucifer"))