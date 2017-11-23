from imdb import IMDb
ia = IMDb()
r=input("Please insert a movie name")

#deadpool
def companyInfo(movie):
    s = ia.search_movie(movie)
    dp = s[0]
    ia.update(dp)
    return (dp.get('production companies'))
def getCast(moviee):
    moviee = ia.get_movie(moviee)
    actor = movie['cast']
#Printing the first 2 persons of cast

    for i in actor[:2]:
        for j in ia.search_person(str(i))[:1]:
            return i

     #actorListstr=str(actorList)#print (i, j.personID)
#Gives other movies in which the first actor played.       
#full_person = ia.get_person(actor[0].getID(), info=["filmography"])
#full_person.keys()
#print(full_person["actor"])

print(getCast('0816692'))
