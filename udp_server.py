from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
try:                                             
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        serverSocket.sendto(message, clientAddress) 
except KeyboardInterrupt:                        
    print("Server shutting down")
finally:                                          
    serverSocket.close()
