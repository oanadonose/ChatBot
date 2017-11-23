from imdb import IMDb
ia = IMDb()
import random
def get_top10movies():
    strresult=""
    top250 = ia.get_top250_movies()
    #print(top250)
    for i in range (10):
        strresult=strresult+"," +str(top250[i])
    return strresult
#print (get_top250())
def get_random10movies():
    strresult=""
    top250 = ia.get_top250_movies()
    #print(top250)
    #in-place shuffle
    random.shuffle(top250)
    result=top250[0:10]
    for i in range(10):
        strresult=strresult+','+str(result[i])
        
    return strresult
print (get_random10movies())
