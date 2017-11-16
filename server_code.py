import socket
import time
import random
from imdb import imdb
from MovieID import movieSearch
i=imdb.IMDb(accessSystem='http')
 
def Main():
	#Give ChatBot server an IP address and port
	host = "127.0.0.1"
	port = 5001
	#Create Socket and bind server to socket           
	thisSocket = socket.socket()
	thisSocket.bind((host,port))
	#Listen for clients     
	thisSocket.listen(1)
	#Connect to client
	conn, addr = thisSocket.accept()
	#print Connect ip address
	print ("The Connection ip is : " + str(addr))
	#Repeat forever
	
	##################List of terms####################
	searchTerms = ['search','find']
	movieTerms = ['movie','film']
	idTerms = ['id']		
	
	###################################################
	filmIDSearch = 0	
	#################Flag Resets###############
	flagSearch = 0
	flagMovie = 0
	flagID = 0
	############################################# 


	while True:
				#Receive info from client
				
				receiveMessDecode = conn.recv(1024).decode()
				receiveMess = receiveMessDecode.lower() #Converts input to lowercase
				log = open ("log.txt","w")
				log.write("\n" + "Server: " + receiveMess)
				receiveWords = receiveMess.split()
				#if no info from client end loop
				
				#If no message recieved
				if not receiveMess:
									break
				
				#################Flag Settings#################
				if any(word in receiveWords for word in searchTerms):
					flagSearch = 1
				if any(word in receiveWords for word in movieTerms):
					flagMovie = 1
				if any(word in receiveWords for word in idTerms):
					flagID = 1
				#############################################

				#################Responses#################
				if filmIDSearch == 1: #If asking user for movie title for movieID 
					returnMess = str(movieSearch(str(receiveMess)))
					filmIDSearch = 0
				elif flagSearch == 1 and flagMovie == 1 and flagID == 1: #User asking for movie ID
					filmIDSearch = 1 #Starts asking user for film title
					returnMess = "What movie ID would you like to search for? "	
				elif flagSearch == 1 and flagMovie == 1: 
					returnMess = 'Search Pass' 
				else:
					returnMess = 'No' #NEED TO CHANGE THIS
				###################################################

					#Print info from client
				print ("Message from User to Chatbot : " + str(receiveMess))
					#set return message
				log.write("\n" + "Client: " + returnMess)
				conn.send(returnMess.encode())                            
	log.close()	
	conn.close()                
if __name__ == '__main__':
			Main()


