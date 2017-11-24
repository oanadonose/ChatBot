from imdb import IMDb

def chatbotMovieDetails(title):
    ''' Function to search for a movie based on the input from the chatbot and returns a selection of useful information'''
    i = IMDb('http')
    movieSearch = i.search_movie(title)
    try:
        movieName = movieSearch[0]
    except IndexError:
        return("Sorry, I could not find the film you were looking for") #Checks if the entry can find any films under the entered name
    movieName = movieSearch[0]
    i.update(movieName)
    movieID = i.get_movie(movieName.getID()) #this section returns all the details about the movie(Genre, Plot, Runtime, Parental Rating/Certificate and URL)
    #print (movieID.keys()) - allows me to check what keys I can search with.
    try:
        genre = str((movieID['genres']))
        replaceGenre = str(genre).replace("[","").replace("]","").replace("'","")#removes punctuation from imdb format
        returnInfo =(str(movieName) + " is a movie that includes the genres " +str(replaceGenre))
        plot = (movieID['plot outline'])
        returnInfo = returnInfo + ("\nThe plot of " + str(movieName) + " is that "+ str(plot))
        runtime = (movieID['runtime'])
        returnInfo = returnInfo + ("\nThe runtime of " + str(movieName) + " is " + str(runtime[0]) + " minutes")
        certificates = (movieID['mpaa'])
        returnInfo = returnInfo + ("\nThe certificate for " + str(movieName) + " is  "+ str(certificates))
        imURL = i.get_imdbURL(movieID)
        returnInfo = returnInfo + ("\n") + imURL
        
    except KeyError:
        return("Hmm, it seems there isn't enough information available on this movie")
    return (returnInfo)

chatbotMovieDetails("Interstellar") #- test
