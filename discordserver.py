#USES DISCORDPY AND IMDBPY

import random
from imdb import imdb
from MovieID import movieSearch
import discord
import asyncio
import random
from castlist import castGet
from castlist import roleSearch,actorNum, vK, MovieKeep
from moreInformation2 import moreInfo
from tvSeries import seasonsEpisodesCounter, listOfEpisodes, infoAboutEpisode
from Top10movies import get_top10movies
from Top10movies import get_random10movies
from rating import getRating
from rating import searchKeyword
from chatbotActorSearch import chatActorSearch
from NewMovieDetails import chatbotMovieDetails
from directorrr import directorGet
from Companyinfo import companyInfo
from Bottom100movies import get_worst10bottom
from Bottom100movies import get_random10bottom

client = discord.Client()
class gV():
    #Defines the class of globalVariables, must start any refernece to these variables with gV.
    ##################List of terms####################
    searchTerms = ['search','find','know', 'information','info']
    movieTerms = ['movie','film']
    idTerms = ['id']    
    castTerms = ['cast']
    whoTerms = ['who','which']
    playTerms = ['play']
    tvSeriesTerms = ['series','tvseries','show']
    episodeTerms = ['episode','episodes']
    directorTerms = ['director','directed']
    companyTerms=['company']
    recoTerms =['reco', 'recommendation','recommendate','recommendated','recommende']
    bottomMovieTerms=['bottom','bad']
    ratingTerms = ['rating']
    keywordTerms = ['about', 'including']
    detailTerms = ['plot', 'story','details']
    actorTerms = ['actor', 'actress']
    greetingsTerms = ['hello','hi','hey','heyy','greetings']
    goodbyeTerms = ['bye','peace','cya','goodbye']
    roleTerms = ['role','roles']
    ##################################################


    ####################Defaults######################
    filmIDSearch = 0
    castSearch = 0
    castNumPull = 0
    specificMovieSearch = 0
    titleStore = ''
    tvSeriesSearch = 0
    series = ''
    wrongChoice = "Why did you choose that? There were only two options!!!!"
    seasonNumber = 0
    episodeNumber = 0
    getdire = 0
    getTop = 0
    company = 0
    ratingTitleSearch = 0
    ratingSearch=0
    actorSearch = 0
    detailSearch = 0
    roleActSearch = 0
    moreInfo = 0
    ##################################################


    #################Flag Resets#################
    flagSearch = 0
    flagMovie = 0
    flagID = 0
    flagCast = 0
    flagPlay = 0
    flagWho = 0
    flagSeries = 0
    flagList = 0
    flagCounter = 0
    flagYN1 = 0
    flagYN2 = 0
    flagN1 = 0
    flagN2 = 0
    flagSeriesSeason = 0
    flagSeriesEpisode = 0
    flagReco = 0
    flagBottom = 0
    flagBot2 = 0
    flagDirect = 0
    flagTop = 0
    flagCompany = 0
    flagTop2 = 0
    flagRating = 0
    flagKeyword = 0
    flagActor = 0
    flagDetail = 0
    flagYN4 = 0
    flagGreetings = 0
    flagGoodbyes = 0
    flagRole = 0
    #############################################

@client.event #Prints a ready message to terminal
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    receiveMess = message.content
    receiveWords = receiveMess.lower()
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    else:
        try:
            #################Flag Settings#################
            if any(word in receiveWords for word in gV.greetingsTerms):
                gV.flagGreetings = 1
            if any(word in receiveWords for word in gV.goodbyeTerms):
                gV.flagGoodbyes = 1
            if any(word in receiveWords for word in gV.searchTerms):
                gV.flagSearch = 1
            if any(word in receiveWords for word in gV.movieTerms):
                gV.flagMovie = 1
            if any(word in receiveWords for word in gV.idTerms):
                gV.flagID = 1
            if any(word in receiveWords for word in gV.castTerms):
                gV.flagCast = 1
            if any(word in receiveWords for word in gV.whoTerms):
                gV.flagWho = 1
            if any(word in receiveWords for word in gV.playTerms):
                gV.flagPlay = 1
            if any(word in receiveWords for word in gV.tvSeriesTerms or gV.episodeTerms):
                gV.flagSeries = 1
            if any(word in receiveWords for word in gV.directorTerms):
                gV.flagDirect = 1
            if any(word in receiveWords for word in gV.companyTerms):
                gV.flagCompany = 1
            if any(word in receiveWords for word in gV.recoTerms):
                gV.flagTop = 1
            if any(word in receiveWords for word in gV.ratingTerms):
                gV.flagRating = 1
            if any(word in receiveWords for word in gV.keywordTerms):
                gV.flagKeyword = 1
            if any(word in receiveWords for word in gV.detailTerms):
                gV.flagDetail = 1
            if any(word in receiveWords for word in gV.actorTerms):
                gV.flagActor = 1
            if any(word in receiveWords for word in gV.bottomMovieTerms):
                gV.flagBottom = 1   
            if any(word in receiveWords for word in gV.roleTerms):
                gV.flagRole = 1
            #############################################
            if gV.flagGreetings == 1:
                returnMess = random.choice(gV.greetingsTerms)
                gV.flagGreetings = 0
            elif gV.flagGoodbyes == 1:
                returnMess = random.choice(gV.goodbyeTerms)
                gV.flagGoodbyes = 0
            if gV.filmIDSearch == 1: #If asking user for movie title for movieID 
                returnMess = str(movieSearch(receiveMess))
                gV.filmIDSearch = 0
            elif gV.detailSearch == 1:
                returnMess = str(chatbotMovieDetails(receiveMess)) + "\n" + str(moreInfo(receiveMess))
                gV.detailSearch = 0
            elif gV.moreInfo == 1:
                if receiveMess == "yes" or receiveMess == "Yes" or receiveMess == "y" or receiveMess == "yes please" or receiveMess == "Y":
                    returnMess = str(chatbotMovieDetails(vK.movieKeep.get()))
                    gV.moreinfo = 0
                else: 
                    returnMess = "Okay."
                    gV.moreInfo = 0    
            elif gV.roleActSearch == 1: #Once user inputted title of movie, gives ACTOR as ROLE string
                gV.roleActSearch = 0
                returnMess = (str(actorNum(receiveWords)) + "\n" + "\n" + "Would you like more info?")
                gV.moreInfo = 1
            elif gV.flagDetail == 1 and gV.flagMovie == 1:
                gV.detailSearch = 1
                returnMess = "What movie would you like some information about?"
                gV.flagDetail = 0
                gV.flagMovie = 0
            elif gV.actorSearch == 1:
                returnMess = str(chatActorSearch(receiveMess))
                gV.actorSearch = 0
            elif gV.flagActor == 1 and gV.flagSearch == 1:
                gV.actorSearch = 1
                returnMess = "What actor would you like some information about?"
                gV.flagActor = 0
                gV.flagSearch = 0
            elif gV.flagBottom == 1:
                        returnMess="Do you want the worst ten movies or random 10 movies from worst top 100? Worst10/Random"
                        gV.flagBot2 = 1
                        gV.flagBottom = 0
            elif gV.flagBot2 == 1:
                if receiveMess == "Worst10" or receiveMess == "worst10" or receiveMess == "Worst10":
                        returnMess = str(get_worst10bottom())
                elif receiveMess == "Random" or receiveMess == "random":
                        returnMess =str(get_random10bottom())
                else:
                    returnMess ="Sorry, please respect the input forms"
                    gV.flagBot2 = 0
            elif gV.flagTop == 1:
                returnMess="Do you want the first 10 movies or 10 random movies from the top of 250 movies?first 10/random"
                gV.flagTop2 = 1
                gV.flagTop = 0   
            elif gV.flagTop2 == 1:
                if receiveMess== "first10":
                    returnMess= str(get_top10movies())
                elif receiveMess== "random":
                    returnMess=str(get_random10movies())
                else:
                    returnMess= "Sorry, please respect the input forms" 
                    gV.flagTop2 = 0
            elif gV.flagDirect == 1:
                gV.getdire=1
                returnMess="What movie are you interested to know the director?" 
            elif gV.flagCompany == 1:
                returnMess="What movie are your looking for company info?"
                gV.company = 1
                gV.flagCompany =0
            elif gV.company == 1:
                returnMess=str(companyInfo(receiveMess))
                gV.company=0
            elif gV.getdire == 1:
                returnMess =str(directorGet(receiveMess))
                gV.getdire =0   
            elif gV.castNumPull == 1:
                gV.castNumPull = 0
                gV.castSearch = 1
                gV.titleStore = receiveMess
                returnMess = "How many cast members do you want listed? "
            elif gV.ratingSearch == 1:
                gV.ratingSearch = 0
                gV.flagRating = 0
                returnMess = str(getRating(str(receiveMess)))
            elif gV.castSearch == 1:
                castNum = receiveMess
                returnMess = str(castGet(gV.titleStore,int(castNum)))
                gV.castSearch = 0
                gV.flagSearch = 0
                gV.flagCast = 0
            elif gV.flagWho == 1 and gV.flagPlay ==1: #If ask for specific actor's role in film
                returnMess = (str(roleSearch(receiveMess)))
                gV.flagWho = 0
                gV.flagPlay = 0
            elif gV.flagSearch == 1 and gV.flagMovie == 1 and gV.flagID == 1: #User asking for movie ID
                gV.filmIDSearch = 1 #Starts asking user for film title
                returnMess = "What movie ID would you like to search for? " 
                gV.flagSearch = 0
                gV.flagMovie = 0
                gV.flagID = 0
            elif gV.flagSearch == 1 and gV.flagCast == 1: 
                gV.castNumPull = 1
                returnMess = "What movie would you like to search for the cast members of?"
            elif gV.flagKeyword==1 and gV.flagMovie == 1 and gV.flagSearch == 1:
                returnMess = str(searchKeyword(str(receiveMess)))
                gV.flagKeyword = 0
                gV.flagMovie = 0
                gV.flagSearch = 0
            elif gV.flagSearch == 1 and gV.flagMovie == 1: 
                returnMess = "What movie would you like to search for?"
                gV.specificMovieSearch = 1
                gV.flagSearch = 0
                gV.flagMovie = 0
            elif gV.specificMovieSearch == 1:
                returnMess = str(moreInfo(receiveMess))
                gV.specificMovieSearch = 0
            elif gV.flagSeries == 1:
                returnMess = str("what is the series that you'd like to search for?")
                gV.flagSeries = 0
                gV.flagCounter = 1
            elif gV.flagCounter == 1:
                gV.series = str(receiveMess)
                seasons,episodes = seasonsEpisodesCounter(receiveMess)
                returnMess = moreInfo(gV.series) + "\n" + "The series you've searched for has " + str(seasons) + " `seasons` and " + str(episodes) + " `episodes`.\nWould you like to see a list of the seasons and episodes?(y/n)"
                gV.flagYN1 = 1  #keeps track of the question with yes/no 
                gV.flagCounter = 0
            elif gV.flagYN1 == 1:
                if receiveMess == "y":
                    returnMess = str(listOfEpisodes(gV.series))
                elif receiveMess == "n":
                    returnMess = "Ok.Would you like to see info about a specific episode? (y/n)"
                    gV.flagN1 = 1 #keeps track of 'no' answer
                    #gV.flagYN3 = 1 #declare
                else:
                    returnMess = gV.wrongChoice
                gV.flagYN1 = 0 
            elif gV.flagYN4 == 1:
                if receiveMess == "y":
                    returnMess = "Ok. Season Number? "
                    gV.flagSeriesSeason = 1
                    gV.flagYN4 = 0
                elif receiveMess == "n":
                    returnMess = "ok no probs"
                else:
                    returnMess = gV.wrongChoice
                flagYN4 = 0
            elif gV.flagN1 == 1:
                if receiveMess == "y":
                    returnMess = "Ok. Season number? "
                    gV.flagSeriesSeason = 1 
                elif receiveMess == "n":
                    returnMess = "ok no probs"
                else:
                    returnMess = gV.wrongChoice
                gV.flagN1 = 0
            elif gV.flagSeriesSeason == 1:
                if receiveMess.isdigit():
                    gV.seasonNumber = int(receiveMess)
                    returnMess = "Episode Number? "
                    gV.flagSeriesEpisode = 1 
                else:
                    returnMess = "You should have input a digit. "
                gV.flagSeriesSeason = 0
            elif gV.flagSeriesEpisode == 1:
                if receiveMess.isdigit():
                    gV.episodeNumber = int(receiveMess)
                    try:
                        returnMess = infoAboutEpisode(gV.series, gV.seasonNumber,gV.episodeNumber)
                    except KeyError:
                        returnMess = "That doesn't exist."
                gV.flagSeriesEpisode = 0
            elif gV.flagList == 1:
                returnMess = listOfEpisodes(gV.series)
                gV.flagList = 0
            elif receiveMess == 'debug':
                returnMess = receiveMess + receiveWords
            elif gV.flagRating==1:
                 gV.ratingSearch = 1
                 returnMess = "Which movies rating are you looking for? "
            elif gV.flagActor == 1 and gV.flagRole == 1:
                returnMess = "For which film?"
                gV.roleActSearch = 1
            else:
                returnMess = "I'm sorry, I didn't understand." #Error catch
        except Exception as e :
            e.args = (e.args[0] + '',)
            returnMess = "An error occured"
            yield from client.send_message(message.channel, returnMess)
            raise


        yield from client.send_message(message.channel, returnMess)

#Team member selection to allow individual testing.
teamMember = input ("Who are you? ")
if teamMember == "Luke":
    client.run('MzgxMDM3NzAyNzEzNDQyMzA0.DPBmiA.74kzIvLmGPBXIP2Hm0wpHr6h3_k') #LUKE
elif teamMember == "Rob":
    client.run('MzgyOTgwNzIyMDkwMzExNjgx.DPe9HA.M1rcJj26j6u8TK_CtlqEWdAbt4E') #ROB
elif teamMember == "Charlie":
    client.run('MzgyODYxMzI5Nzc5OTE2ODAw.DPb31g.oa5a949IIMDIZQZzvYbdtFZ9Ouc') #CHARLIE
elif teamMember == "Oana":
    client.run('MzgyODc3NDU4ODM3NTM2Nzc0.DPcF9Q.36FobsXCFEuUlSGPfV8ar28wVo8') #OANA
elif teamMember == "Andreea":
    client.run('MzgyOTExODgyNzg2NTA0NzA3.DPcmDA.JhE5dXE7pHwFYCS0qyncB9nNMnA') #ANDREEA
elif teamMeber == "Ibk":
    client.run('PUT BOT TOKEN HERE') #IBK
else:

    print("Unknown user, type either: Luke, Rob, Charlie, Oana, Ibk or Andreea")
