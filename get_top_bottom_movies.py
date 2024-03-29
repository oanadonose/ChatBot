
""" get_top_bottom_movies.py
Usage: get_top_bottom_movies
Return top and bottom 10 movies, by ratings.
"""
import sys
import imdb
i = imdb.IMDb()
top250 = i.get_top250_movies()
bottom100 = i.get_bottom100_movies()

out_encoding = sys.stdout.encoding or sys.getdefaultencoding()

for label, ml in [('top 10', top250[:10]), ('bottom 10', bottom100[:10])]:
    
    print ('%s movies' % label)
    print ('rating\tvotes\ttitle')
    for movie in ml:
        outl = u'%s\t%s\t%s' % (movie.get('rating'), movie.get('votes'),
                                    movie['long imdb title'])
        print (outl.encode(out_encoding, 'replace'))

