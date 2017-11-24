from imdb import IMDb

def chatActorSearch(actor):
    '''This function searches for an actor that is input from the chatbot and returns a selection of details about the actor'''
    i = IMDb('http')
    actorSearch = i.search_person(actor)
    try: #checks to see if the actor can be found on imdb
        actorName = actorSearch[0]#gets the first actor(most popular) from the list
    except:
        return ("Sorry, I could not find the actor you were looking for")
    i.update(actorName)
    actorID = i.get_person(actorName.getID()) #this section returns all the details about the movie
    (actorID.keys())
    try: #checks if there are any key errors
        returnInfo = (str(actorName) + "'s full name is " + actorID['birth name'])
        returnInfo = returnInfo + ('\n' + str(actorName) + " has a height of " + actorID['height'])
        returnInfo = returnInfo + ('\n' + str(actorName) + "'s birthday is on " + actorID['birth date'])
        actorInfo = actorID["actor"]
        actorList = []
        try: #checks if 10 roles can be found, if not outputs error message with rest of the details.
            for a in actorInfo:
                actorList.append(a['title'])
                if len(actorList) == 10:
                    break
        except IndexError:
            actorList = ("Sorry, no roles found")
        finalActor = str(actorList).replace("['",'').replace("'","").replace("]","")
        returnInfo = returnInfo + ('\n' + str(actorName) + "' last 10 roles include \n" + str(finalActor) +"\n")#cannot get imdbpy to print without added details               
        #print(actorID.key2infoset) - lets me check what I can search for about an actor
        imURL = i.get_imdbURL(actorID) #retrieves the imdb url link for the actor
        returnInfo = returnInfo + ("If you want to look more into " + str(actorName) + " then please follow this link below: \n" + imURL)
        return (returnInfo)
    except KeyError:
        return ("Huh, it seems there isn't enough information available on this actor")


#chatActorSearch('andrew ') - test
