from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
try:                                             
    while True:
        connectionSocket, addr = serverSocket.accept()
        try:                                      
            sentence = connectionSocket.recv(1024).decode()
            connectionSocket.send(sentence.encode())   
        except ConnectionResetError:                
            print('Client disconnected')
        connectionSocket.close()
except KeyboardInterrupt:                          
    print('Server shutting down')
finally:                                            
    serverSocket.close()
