from imdb import IMDb
ia = IMDb()
def get_top10movies():
    strresult=""
    top250 = ia.get_top250_movies()
    #print(top250)
    for i in range (10):
        strresult=strresult+"," +str(top250[i])
    return strresult
#print (get_top250())
