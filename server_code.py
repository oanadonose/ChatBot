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
	filmIDSearch = 0		
	while True:
				#Receive info from client
				receiveMess = conn.recv(1024).decode()
				log = open ("log.txt","a")
				log.write("\n" + Server: " + receiveMess)
				receiveWords = receiveMess.split()
				#if no info from client end loop
				if not receiveMess:
									break
				if filmIDSearch == 1: #If asking user for movie title for movieID 
					returnMess = str(movieSearch(str(receiveMess)))
					filmIDSearch = 0
				elif ('search' in receiveWords or 'find' in receiveWords) and ('film' in receiveWords or 'movie' in receiveWords) and ('ID' in receiveWords): #User asking for movie ID
					filmIDSearch = 1 #Starts asking user for film title
					returnMess = "What movie ID would you like to search for? "	
				elif 'search' in receiveWords or 'find' in receiveWords: #Test code
					returnMess = 'Search Pass' 
				else:
					returnMess = 'No' #NEED TO CHANGE THIS
					#Print info from client
				print ("Message from User to Chatbot : " + str(receiveMess))
					#set return message
				log.write("\n" + Client: " + returnMess)
				conn.send(returnMess.encode())                             
	log.close()	
	conn.close()                
if __name__ == '__main__':
			Main()

