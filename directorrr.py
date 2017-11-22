from imdb import IMDb
ia = IMDb()

movie = ia.get_movie('0816692')
print ("Name of the movie: ", movie)
for i in movie['director']:
    print ("Director: ", i)
    director = ia.search_person(i["name"])[0]
    ia.update(director)
    print ("Movies directed by %s:" % director)
    for movie_name in director["director movie"]:
        print (movie_name)
