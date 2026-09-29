from socket import *
serverName = '192.168.10.254'             
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)                        
message = input('Input a message: ')
if message == '':                                  
    print('Message cannot be empty')
else:
    try:                                           
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print('From Server:', modifiedMessage.decode())
    except TimeoutError:                           
        print('No response from server (timed out)')
clientSocket.close()
