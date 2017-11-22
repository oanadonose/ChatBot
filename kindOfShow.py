from imdb import IMDb
from MovieID import movieSearch

i = IMDb()

#Testing-------------------------------------------------------------
#title = input(" >*>")
#--------------------------------------------------------------------

def determineKind(title):
	titleID = movieSearch(title)
	m = i.get_movie(str(titleID))
	kind = m['kind']
	return kind

#print (determineKind(title))
