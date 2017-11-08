import imdb
from imdb import IMDb
ia = IMDb('http')
imdb_access = imdb.IMDb()
#i = imdb.IMDb(accessSystem='http')
#title=raw_input("Which film would you like to watch today?")
#movie_list = i.search_movie('title')
#print (movie_list)
ia = IMDb('http')



keyTitle=raw_input("Hello!Are you searching a movie? Y/N")
if keyTitle=="N":
    print("Sorry, I don't have how to help you today.See you.")
elif keyTitle!="N" and keyTitle!="Y":
    print("Please respect the specific type of answer,thank you.")        
else:
    key=raw_input("Are you searching a specific movie or do you want a random one? Y/Random")
    if(key=="Y"):
       keyTitle=raw_input("Please input a keyword or the movie title.")
       print ("Here are some relative movies with regarding your search.")
       print ia.search_keyword(keyTitle)
       preciseTitle=raw_input("Would you like to be more precise?Y/N")
       if preciseTitle=="N":
           print ("Ok then. Hope u enjoy it!")
       elif preciseTitle=="Y":
           preciseTitle=raw_input("Ok then, please input some more words or the entire title of the movie.")
           print("Here are the outputs regarding your search.")
           print ia.search_keyword(preciseTitle)
    elif(key=="Random"):
        import requests
        import re
 
        top250_url = "http://akas.imdb.com/chart/top"
 
        def get_top250():
            r = requests.get(top250_url)
            html = r.text.split("\n")
            result = []
            for line in html:
                line = line.rstrip("\n")
                m = re.search(r'data-titleid="tt(\d+?)">', line)
                if m:
                    _id = m.group(1)
                    result.append(_id)
                #
            return result



