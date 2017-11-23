from imdb import IMDb
ia = IMDb()
#r=input("Please insert a movie name")
    """Takes a movie title as input and returns production company info"""

#deadpool
def companyInfo(movie):
    s = ia.search_movie(movie)
    dp = s[0]
    ia.update(dp)
    return (dp.get('production companies'))
