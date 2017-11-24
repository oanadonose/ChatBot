from imdb import IMDb
ia = IMDb()
from MovieID import movieSearch
#title=input("please input movie name")
def directorGet(title):
    #transforms movie title in movie id in order to search the director
    movieid=movieSearch(title)
    movie=ia.get_movie(movieid)
    director=movie['director']
    #returns the first director
    return director[0]['name']

#print(directorGet("Titanic"))
