from imdb import IMDb
ia = IMDb()
import random
#gets top250 then returns first 10 movies

def get_worst10bottom():
    strresult=""
    bottom100 = ia.get_bottom100_movies()
    #print(bottom100)
    for i in range (10):
        strresult=strresult+"," +str(bottom100[i])
    return strresult
#print (get_worst10bottom())

#gets top250 thand returns random 10 movies 
def get_random10bottom():
    strresult=""
    bottom100 = ia.get_bottom100_movies()
    #print(bottom100)
    #in-place shuffle
    random.shuffle(bottom100)
    result=bottom100[0:10]
    for i in range(10):
        strresult=strresult+','+str(result[i])
        
    return strresult
#print (get_ramdom10bottom())
