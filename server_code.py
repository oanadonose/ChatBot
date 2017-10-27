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
                GreetingsKeywords = ["hi","hello","sup","whatsup","greetings","what's up?","greetings"]
                GreetingsResponses = ["hi","*stares at you blankly*","hello","greetings","good day","hey"]

                
                def GREETINGS(receiveMess):
                    if receiveMess in GreetingsKeywords:
                        greeting = 1
                        response = random.choice(GreetingsResponses)
                        return response

                GoodbyeKeywords = ["bye","bai","peace","see you"]
                GoodbyeResponses = ["cya","bye"]
                def GOODBYES(receiveMess):
                    if receiveMess.lower() in GoodbyeKeywords:
                        goodbye = 1
                        response = random.choice(GoodbyeResponses)
                        return response
                if (GOODBYES(receiveMess)):
                     returnMess = GOODBYES(receiveMess)
                elif (GREETINGS(receiveMess)):
                     returnMess = GREETINGS(receiveMess)
                print(returnMess)                   
                conn.send(returnMess.encode())                             
    conn.close()                
if __name__ == '__main__':
            Main()







            
