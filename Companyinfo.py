from imdb import IMDb
from MovieID import movieSearch
i = IMDb()

def productionCompanyGet():
    s = movieSearch(movieTitle)
    dp = s[0]
    i.update(dp)
    print (dp.get('production companies'))


def otherMoviesPlayedIn():
    movie = i.get_movie(movieSearch(movieTitle))
    actor = movie['cast']
    #Printing the first 2 persons of cast
    #print ("Cast: ")
    #for i in actor[:2]:
        #for j in ia.search_person(str(i))[:1]:
            #print (i, j.personID)
    #Gives other movies in which the first actor played.       
    full_person = ia.get_person(actor[0].getID(), info=["filmography"])
    full_person.keys()
    print (full_person["actor"])

