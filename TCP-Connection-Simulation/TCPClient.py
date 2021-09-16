from socket import *

# Question 3 - sent string, then receive reward based on table 1.

# Specify server name (localhost) and port used
serverName = '127.0.0.1'
serverPort = 12000

# create socket for TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# prompts user to enter string, encodes it, then sends it to server, 
# receives it via a buffer, then decodes it and prints it out

sentence = input('Input a string:')
clientSocket.send(sentence.encode())
reward = clientSocket.recv(1024)
print('From Server: ', reward.decode())

# closes connection
clientSocket.close()