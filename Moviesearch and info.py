from imdb import IMDb

def newMovieDetails(title):
    '''This function searches for a film, asks if the user wants to know more information, outputs movie information or returns to chatbot loop'''
    i = IMDb('http')
    movieSearch = i.search_movie(title)
    count = 0
    retry = 0
    try:
        errorCheck = (movieSearch[count])
    except IndexError:
        errorTitle = input("I can't think of any films like that... Could you try again? \n")
        movieSearch = i.search_movie(errorTitle) #when no films can be found, asks user to enter a new film name and recalls the function
    while retry != 1:
        try:
            print (movieSearch[count])
        except IndexError:
            endFunc = input("Hey, the list is finished...") #when no more movies are found, handles error and returns the user to the main chatbot
            break
        trFalse = input ("Is this the movie you were looking for?  ")
        noWords = ['no', 'nah', 'n', 'nope', 'No', 'Nah', 'N', 'Nope','STOP']
        if any(word in trFalse for word in noWords): #checks if the user responds no when checking if the film is right and continues to return another film
            count = count + 1
            if trFalse == 'STOP':
                print ("Would you like to ask me something else? ")
                break
            if count == 5:
                print("\nHey it looks like I'm struggling to find the film for you. If you want to ask me something else, just tell me to 'STOP'? \n")
        else:
            try:
                print("Okay great")
                movieName = movieSearch[count]
                retry = 1
                movieInfo = input ("Would you like to know more about  " + str(movieName) + "? ")
                noWords = ['no', 'nah', 'n', 'nope', 'No', 'Nah', 'N', 'Nope']
                if any(word in movieInfo for word in noWords):
                    print ("Would you like to ask me something else?")
                    break
                else:
                    i.update(movieName)
                    movieID = i.get_movie(movieName.getID()) #this section returns all the details about the movie(Genre, Plot, Runtime, Parental Rating/Certificate)
                    #print (movieID.keys()) - allows me to check what keys I can search with.
                    genre = str((movieID['genres']))
                    replaceGenre = str(genre).replace("[","").replace("]","").replace("'","")
                    print (str(movieName) + " is a movie that includes the genres " +str(replaceGenre))
                    plot = (movieID['plot outline'])
                    print ("The plot of " + str(movieName) + " is that "+ str(plot))
                    runtime = (movieID['runtime'])
                    print ("The runtime of " + str(movieName) + " is " + str(runtime[0]) + " minutes")
                    certificates = (movieID['mpaa'])
                    print ("The certificate for " + str(movieName) + " is  "+ str(certificates))
            except KeyError:
                print ("Sorry I don't think there is enough information on this movie")

newMovieDetails('inception')
