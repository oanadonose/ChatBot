from imdb import IMDb
i = IMDb()

title = raw_input('Input Title ') 

def movieData(title):
        '''A function that takes the movie name input from the user, searches for it and returns details about the film such as the genre'''
        i = IMDb()
        #print i.get_movie_infoset()
        f = i.search_movie(title)
        m = f[0]
        i.update(m)
        fullSummary = m.summary()
        splitSummary = fullSummary.split()
        joinSummary = ' '.join(splitSummary)
        replaceSummary = joinSummary.replace("(u", "").replace("Movie ===== Title: ","").replace("Genres:", " genre list includes").replace("Director:", ". \nThe directors of the movie include").replace("Writer:", " \nThe writers include").replace("Cast:", " \nThe cast includes").replace("Runtime:", " \nThe movie runtime in minutes is").split("Country", 1)[0]
        print fullSummary
        print replaceSummary
        
movieData(title)
