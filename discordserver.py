import random
from imdb import imdb
from MovieID import movieSearch
import discord
import asyncio
from castlist import castGet
from castlist import roleSearch
from moreInformation2 import moreInfo
from tvSeries import seasonsEpisodesCounter, listOfEpisodes, infoAboutEpisode
#from directorrr import directorGet
#from Companyinfo import companyInfo

client = discord.Client()
class gV(): #Defines the class of globalVariables, must start any refernece to these variables with gV.
	##################List of terms####################
	searchTerms = ['search','find']
	movieTerms = ['movie','film']
	idTerms = ['id']    
	castTerms = ['cast']
	whoTerms = ['who']
	playTerms = ['play']
	tvSeriesTerms = ['series','tvseries','show']
	directorTerms = ['director','directed']
	companyTerms=['company']
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
	flagDirect = 0
	flagTop = 0
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
			if any(word in receiveWords for word in gV.tvSeriesTerms or gV.episodeTerms):
				gV.flagSeries = 1
			if any(word in receiveWords for word in gV.directorTerms):
				gV.flagDirect = 1
			if any(word in receiveWords for word in gV.companyTerms):
				gV.flagCompany = 1
			#############################################
			if gV.filmIDSearch == 1: #If asking user for movie title for movieID 
				returnMess = str(movieSearch(receiveMess))
				gV.filmIDSearch = 0
			elif gV.flagDirect == 1:
				gV.getdire=1
				returnMess="What movie are you interested to know the director?InputID"	
			elif gV.flagCompany == 1:
				returnMess="What movie are your looking for company info?"
				gV.company = 1
				gV.flagCompany =0
			elif gV.company == 1:
				eturnMess=str(companyInfo(receiveMess))
				gV.company=0
			elif gV.getdire == 1:
				returnMess =str(directorGet(receiveMess))
				gV.getdire =0	
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
				gV.flagSearch = 0
				gV.flagMovie = 0
				gV.flagID = 0
			elif gV.flagSearch == 1 and gV.flagCast == 1: 
				gV.castNumPull = 1
				returnMess = "What movie would you like to search for the cast members of?"
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
				returnMess = "The series you've searched for has " + str(seasons) + " `seasons` and " + str(episodes) + " `episodes`.\nWould you like to see a list of the seasons and episodes?(y/n)"
				gV.flagYN1 = 1  #keeps track of the question with yes/no 
				gV.flagCounter = 0
			elif gV.flagYN1 == 1:
				if receiveMess == "y":
					returnMess = str(listOfEpisodes(gV.series))
				elif receiveMess == "n":
					gV.flagN1 = 1 #keeps track of 'no' answer
					returnMess = "Ok.Would you like to see info about a specific episode? (y/n)"
					#gV.flagYN3 = 1 #declare
				else:
					returnMess = gV.wrongChoice
				gV.flagYN1 = 0 
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
