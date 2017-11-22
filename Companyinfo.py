from imdb import IMDb
ia = IMDb()
r=input("Please insert a movie name")
s = ia.search_movie('Deadpool')
dp = s[0]
ia.update(dp)
print (dp.get('production companies'))

movie = ia.get_movie('1375666')
actor = movie['cast']
#Printing the first 2 persons of cast
print ("Cast: ")
for i in actor[:2]:
    for j in ia.search_person(str(i))[:1]:
        print (i, j.personID)
#Gives other movies in which the first actor played.       
full_person = ia.get_person(actor[0].getID(), info=["filmography"])
full_person.keys()
print(full_person["actor"])
