import random
from imdb import imdb
from MovieID import movieSearch
from castlist import castGet
import discord
import asyncio

client = discord.Client()
class gV(): #Defines the class of globalVariables, must start any refernece to these variables with gV.
    ##################List of terms####################
    searchTerms = ['search','find']
    movieTerms = ['movie','film']
    idTerms = ['id']    
    castTerms = ['cast']    

    ##################################################

    ####################Defaults######################
    filmIDSearch = 0
    castSearch = 0
    castNumPull = 0
    titleStore = ''
    ##################################################


    #################Flag Resets#################
    flagSearch = 0
    flagMovie = 0
    flagID = 0
    flagCast = 0
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
        #################Flag Settings#################
        if any(word in receiveWords for word in gV.searchTerms):
            gV.flagSearch = 1
        if any(word in receiveWords for word in gV.movieTerms):
            gV.flagMovie = 1
        if any(word in receiveWords for word in gV.idTerms):
            gV.flagID = 1
        if any(word in receiveWords for word in gV.castTerms):
            gV.flagCast = 1
        #############################################
        if gV.filmIDSearch == 1: #If asking user for movie title for movieID 
            returnMess = str(movieSearch(receiveMess))
            gV.filmIDSearch = 0
        elif gV.castNumPull == 1:
            gV.castNumPull = 0
            gV.castSearch = 1
            gV.titleStore = receiveMess
            returnMess = "How many cast members do you want listed? "
        elif gV.castSearch == 1:
            castNum = receiveMess
            returnMess = str(castGet(gV.titleStore,int(castNum)))
            gV.castSearch = 0
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
        else:
            returnMess = "I'm sorry, I didn't understand." #Error catch


        yield from client.send_message(message.channel, returnMess)

client.run('MzgxMDM3NzAyNzEzNDQyMzA0.DPBmiA.74kzIvLmGPBXIP2Hm0wpHr6h3_k')
