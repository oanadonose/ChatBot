
from imdb import IMDb
ia = IMDb()
#r=input("Please insert a movie name")
"""Takes a movie title as input and returns production company info"""

#deadpool
def companyInfo(movie):
    strresult=""
    s = ia.search_movie(movie)
    dp = s[0]
    ia.update(dp)
    result=dp.get('production companies')
    for i in range(len(result)):
        strresult=strresult+ "," +str(result[i]['name'])
    return (strresult)
#print (companyInfo("deadpool"))
