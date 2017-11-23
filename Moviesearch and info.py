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
        trFalse = input ("Is this the movie you were looking for?")
        noWords = ['no', 'nah', 'n', 'nope', 'No', 'Nah', 'N', 'Nope','STOP']
        if any(word in trFalse for word in noWords): #checks if the user responds no when checking if the film is right and continues to return another film
            count = count + 1
            if trFalse == 'STOP':
                break
            if count == 5:
                print("\nHey it looks like I'm struggling to find the film for you. If you want to ask me something else, just tell me to 'STOP'? \n")
        else:
            try:
                print("Okay great")
                movieName = movieSearch[count]
                retry = 1
                movieInfo = input ("Would you like some more information on " + str(movieName) + "? ")
                noWords = ['no', 'nah', 'n', 'nope', 'No', 'Nah', 'N', 'Nope']
                if any(word in movieInfo for word in noWords):
                    break
                else:
                    i.update(movieName)
                    movieID = i.get_movie(movieName.getID()) #this section returns all the details about the movie
                    #print (movieID.keys())
                    releaseYear = (movieID['year'])
                    fullTitle = (movieID['smart long imdb canonical title'])
                    print (str(movieName) + " was released in " +str(releaseYear))
                    plot = (movieID['plot outline'])
                    print ("The plot of " + str(movieName) + " is that "+ str(plot))
                    directors = (movieID['director'])
                    directorNum = len(directors)
                    print ("Here are all of the directors for the movie " + str(movieName) + ": \n" + str(directors[directorNum-1]))
                    writers = (movieID['writer'])
                    writerNum = len(writers)
                    print ("Here are all of the writers for the movie " + str(movieName) + ": \n" + str(writers[writerNum-1]))
            except KeyError:
                print ("Sorry I don't think there is enough information on this movie")

newMovieDetails('bee movie')
