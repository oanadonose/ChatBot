from imdb import IMDb
ia = IMDb()
#title=input("please input movie id")
def directorGet(title):
    the_matrix=ia.get_movie(title)
    return the_matrix['director']

#0816692
#print(directorGet("0133093"))
