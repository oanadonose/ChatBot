def actorsearch(act):
    i = IMDb('http')
    actorfilms = i.search_person(act)
    count = 0
    retry = 0
    while retry != 1:
        print actorfilms[count]
        trFalse = raw_input ("Is this the person you were looking for?")
        if trFalse == "no":
            count = count + 1
            if actorfilms[count] == actorfilms[count - 2]:
                print "would you like some help"
        else:
            print "ok"
            retry = 1
            actInfo = raw_input ("Would you like some more information on " + str(actorfilms[count]) +" ? ")
            if actInfo == "yes":
                print actorfilms[count].summary()
