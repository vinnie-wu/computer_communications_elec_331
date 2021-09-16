from socket import *

# specifies port the server uses, creates TCP socket and binds to port
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

# listens to connection (queue limit = 1)
serverSocket.listen(1)

print('This server is ready to receive..')

# upon receival of message
while True:

    # creates socket for TCP connection, receives message and decodes it
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()

    # value of reward based on TABLE-1
    reward = -1
    if sentence == 'A':
        reward = 3
    if sentence == 'B':
        reward = 2
    if sentence == 'C':
        reward = 1 
    print("Reward generated: ", reward)

    # sends reward value to client via TCP (encoded)
    connectionSocket.send(str(reward).encode())

    # terminates connection
    connectionSocket.close()
