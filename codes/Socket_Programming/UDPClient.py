# include Python's socket library
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')

# attach server name, port to message; send to socket
# the transformation of server name to IP address is done by the socket library
clientSocket.sendto(message.encode(), (serverName, serverPort))

# read reply characters form socket into string
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print('From Server:', modifiedMessage.decode())
clientSocket.close()