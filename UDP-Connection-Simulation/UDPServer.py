# UDP Server code - copied from q4
import random
from socket import *

# Create UDP Socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("Waiting to be connected...")

while True:
    # Generate random number
    rand = random.randint(0,49)
    msg, addr = serverSocket.recvfrom(1024)
    msg = msg.upper()

    if rand < 18:
        continue
    serverSocket.sendto(msg,addr)
