from socket import *
serverName = '192.168.10.254'                     
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(5)                          
try:                                                
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input a message: ')
    if sentence == '':                             
        print('Message cannot be empty')
    else:
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From Server:', modifiedSentence.decode())
except (TimeoutError, ConnectionRefusedError):      
    print('Could not reach server')
clientSocket.close()
