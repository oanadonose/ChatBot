import imdb
from imdb import IMDb
ia = IMDb('http')
imdb_access = imdb.IMDb()
#i = imdb.IMDb(accessSystem='http')
#title=raw_input("Which film would you like to watch today?")
#movie_list = i.search_movie('title')
#print (movie_list)
ia = IMDb('http')
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
    return result
print (get_top250())
