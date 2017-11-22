import random
from imdb import imdb
from MovieID import movieSearch
import discord
import asyncio
from castlist import castGet
from castlist import roleSearch
#from gettop250 import get_top250
from Companyinfo import productionCompanyGet
import get_top_bottom_movies
client = discord.Client()
class gV(): #Defines the class of globalVariables, must start any refernece to these variables with gV.
    ##################List of terms####################
    searchTerms = ['search','find']
    movieTerms = ['movie','film']
    idTerms = ['id']    
    castTerms = ['cast']
    whoTerms = ['who']
    playTerms = ['play']
    recommendationTerms = ['recomendation','reco']
    prodCompTerms= ['production', 'company']
    ##################################################

    ####################Defaults######################
    filmIDSearch = 0
    castSearch = 0
    castNumPull = 0
    titleStore = ''
    productionCompanyPull=0
    ##################################################


    #################Flag Resets#################
    flagSearch = 0
    flagMovie = 0
    flagID = 0
    flagCast = 0
    flagPlay = 0
    flagWho = 0
    flagReco = 0
    flagCompany = 0
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
            if any(word in receiveWords for word in gV.recommendationTerms):
                gV.flagReco = 1
            if any(word in receiveWords for word in gV.prodCompTerms):
                gV.flagCompany = 1    
            #############################################
            if gV.filmIDSearch == 1: #If asking user for movie title for movieID 
                returnMess = str(movieSearch(receiveMess))
                gV.filmIDSearch = 0
                gV.productionCompanyPull = 1
            elif gV.castNumPull == 1:
                gV.castNumPull = 0
                gV.castSearch = 1
                gV.titleStore = receiveMess
                returnMess = "How many cast members do you want listed? "
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
            elif gV.flagSearch == 1 and gV.flagCast == 1: 
                gV.castNumPull = 1
                returnMess = "What movie would you like to search for the cast members of?"
            elif gV.flagSearch == 1 and gV.flagMovie == 1: 
                returnMess = 'Search Pass' 
            elif receiveMess == 'debug':
                returnMess = receiveMess + receiveWords
            elif gV.flagSearch == 1 and gV.flagReco == 1:
                returnMess= str((outl.encode(out_encoding, 'replace')))
                gV.flagReco = 0
                gV.flagSearch = 0
            elif gV.flagCompany == 1:
                 gV.flagSearch=1
                 gV.flagMovie=1
                 gV.flagID=1
            elif productionCompanyPull==1:
                 returnMess=str(productionCompanyGet)
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
    client.run('PUT BOT TOKEN HERE') #ROB
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
