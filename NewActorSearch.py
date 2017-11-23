from imdb import IMDb

def actorSearch(actor):
    '''This function searches for an actor, asks if the user wants to know more information, outputs actor information or returns to chatbot loop'''
    i = IMDb('http')
    actorSearch = i.search_person(actor)
    count = 0
    retry = 0
    try:
        errorCheck = (actorSearch[count])
    except IndexError:
        errorActor = input("I can't think of any actors called that... Could you try again? \n")
        actorSearch = i.search_person(errorActor) #when no actors can be found, asks user to enter a different actors name and recalls the function
    while retry != 1:
        try:
            print (actorSearch[count])
        except IndexError:
            endFunc = input("Hey, the list is finished...") #when no more actors are found, handles error and returns the user to the main chatbot
            break
        trFalse = input ("Is this the actor you were looking for? ")
        noWords = ['no', 'nah', 'n', 'nope', 'No', 'Nah', 'N', 'Nope','STOP']
        if any(word in trFalse for word in noWords): #checks if the user responds no when checking if the film is right and continues to return another film
            count = count + 1
            if trFalse == 'STOP':
                break
            if count == 5:
                print("\nHey it looks like I'm struggling to find the actor for you. If you want to ask me something else, just tell me to 'STOP'? \n")
        else:
            try:
                print("Okay great")
                actorName = actorSearch[count]
                retry = 1
                actorInfo = input ("Would you like some more information on " + str(actorName) + "? ")
                noWords = ['no', 'nah', 'n', 'nope', 'No', 'Nah', 'N', 'Nope']
                if any(word in actorInfo for word in noWords):
                    break
                else:
                    i.update(actorName)
                    actorID = i.get_person(actorName.getID()) #this section returns all the details about the movie
                    print (actorID.keys())
                    filmList = len(actorID['actor'])
                    print (str(actorName) + "'s full name is " + actorID['birth name'])
                    print (str(actorName) + " has a height of " + actorID['height'])
                    print (str(actorName) + "'s birthday is on " + actorID['birth date'])
                    print (str(actorName) + " has featured in this list of films \n" + str(actorID["actor"]) +"\n")#cannot get imdbpy to print without added details

                    
                #print(actorID.key2infoset) - lets me check what I can search for about an actor
                imURL = i.get_imdbURL(actorID)
                print ("If you want to look more into " + str(actorName) + " then please follow this link below: \n" + imURL)



            except KeyError:
                print ("Sorry I don't think there is enough information on this actor")


#actorSearch('bill murray') - test
