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
	while True:
				#Receive info from client
				receiveMess = conn.recv(1024).decode()
				receiveWords = receiveMess.split()
				#if no info from client end loop
				if not receiveMess:
									break
				if ('search' in receiveWords or 'find' in receiveWords) and ('film' in receiveWords or 'movie' in receiveWords):
					returnMess = str(movieSearch(receiveWords[2]))
				elif 'search' in receiveWords or 'find' in receiveWords:
					returnMess = 'Search Pass' 
				else:
					returnMess = 'No' 
					#Print info from client
				print ("Message from User to Chatbot : " + str(receiveMess))
					#set return message
				conn.send(returnMess.encode())                             
	conn.close()                
if __name__ == '__main__':
			Main()

