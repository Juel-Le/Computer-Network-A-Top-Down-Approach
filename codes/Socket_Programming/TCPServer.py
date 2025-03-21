from socket import *

serverPort = 12000

# create a TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print('The server is ready to receive')

while True:
    # wait for client connection
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection from {addr} has been established!')
    
    # receive data from the client
    message = connectionSocket.recv(1024).decode()
    modifiedMessage = message.upper()
    
    # send modified data back to the client
    connectionSocket.send(modifiedMessage.encode())
    
    # close the connection with the client
    connectionSocket.close()