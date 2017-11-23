from imdb import IMDb

def actorsearch(act):
    i = IMDb('http')
    actorfilms = i.search_person(act)
    count = 0
    retry = 0
    while retry != 1:
        print (actorfilms[count])
        trFalse = input ("Is this the person you were looking for?")
        if trFalse == "no":
            count = count + 1

        else:
            print ("ok")
            retry = 1
            actInfo = input ("Would you like some more information on " + str(actorfilms[count]) +" ? ")
            if actInfo == "yes":
                finalActor = actorfilms[count]
                i.update(finalActor)
                actorID = i.get_person(finalActor.getID(), info=["filmography", "main","biography"])
                i.update(actorID)
                actorID.keys()

                print (str(finalActor) + "'s full name is " + actorID['birth name'])
                print (str(finalActor) + " has a height of " + actorID['height'])
                print (str(finalActor) + "'s birthday is on " + actorID['birth date'])
                print(str(finalActor) + " has featured in this list of films \n" + str(actorID["actor"]))
                #print(actorID.key2infoset)
                imURL = i.get_imdbURL(actorID)
                print ("If you want to look more into " + str(finalActor) + " then please follow this link below: \n" + imURL)


actorsearch('leonardo di')
