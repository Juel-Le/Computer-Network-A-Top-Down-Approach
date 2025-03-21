from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
# because TCP is connection oriented, we need to connect to the server before sending any data
clientSocket.connect((serverName, serverPort))

message = input('Input lowercase sentence: ')

# since TCP is connection oriented, we can send the message directly
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048)
print('From Server:', modifiedMessage.decode())
clientSocket.close()