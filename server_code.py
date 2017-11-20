import socket
import time
 
 
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
    #Repear forever
    while True:
                #Receive info from client
                receiveMess = conn.recv(1024).decode()
                #if no info from client end loop
                if not receiveMess:
                                    break
                #Print info from client
                print ("Message from receiveMess to Chatbot : " + str(receiveMess))
                #set return message
                
                
                import random
                from imdb import imdb
                i=imdb.IMDb(accessSystem='http')

                GreetingsKeywords = ["hi","hello","sup","whatsup","greetings"]
                GreetingsResponses = ["hi","*stares at you blankly*","hello","greetings","good day","hey"]
                GoodbyeKeywords = ["bye","bai","cya","peace"]
                GoodbyeResponses = ["bye","cya","peace","good day"]
                BestKeywords = ["best","recommendation","good","interesting"]
                  

                greeting=0
                goodbye=0
                countBest=0

                def stringToList(receiveMess):
                    receiveMess = receiveMess.split()
                    for word in receiveMess:
                        for character in word:
                            wordPlace = receiveMess.index(word)
                            if character=="?" or character=="." or character=="," or character=="!":
                                wordGood = word.replace(character,"")
                                receiveMess[wordPlace] = wordGood
                    return receiveMess

                def GREETINGS(receiveMess):
                    for word in receiveMess:
                        if word.lower() in GreetingsKeywords:
                            greeting = 1
                            response = random.choice(GreetingsResponses)
                            return response
                              
                def GOODBYES(receiveMess):
                    for word in receiveMess:
                        if word.lower() in GoodbyeKeywords:
                            goodbye = 1
                            response = random.choice(GoodbyeResponses)
                            return response
                stringToList(receiveMess)
                if (GOODBYES(receiveMess)):
                     returnMess = GOODBYES(receiveMess)
                elif (GREETINGS(receiveMess)):
                     returnMess = GREETINGS(receiveMess)
                else: 
                    returnMess = "Unassigned" #Added to do some error checking. 
                print (returnMess)                
                conn.send(returnMess.encode())                             
    conn.close()                
if __name__ == '__main__':
         Main()
          
