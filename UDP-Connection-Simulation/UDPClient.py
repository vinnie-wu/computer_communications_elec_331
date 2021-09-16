# Client side code, first necessary libraries are imported
from time import *
from socket import *

# Set up localhost
serverName = '127.0.0.1'
# using UDP, so SOCK_DGRAM is used.
clientSocket = socket(AF_INET, SOCK_DGRAM)
# timeout of 2 seconds (per question)
clientSocket.settimeout(2)
# start with packet #1
sequence_number = 1
# collect rtt here in this array
rtt = []

# limit of 20 packets (per question)
while sequence_number <21:
    start = time()

    # initiate time, display message: Ping -- sequence number -- time
    # note time is in system time, upon checking with TA this is accepted.
    message = ('Ping %d %d' %(sequence_number, start))
    clientSocket.sendto(message.encode(), (serverName, 12000))
    try: 
        # calculate time and print upon receival of packet.
        message, address = clientSocket.recvfrom(1024)
        elapsed = (time() - start)
        rtt.append(elapsed)
        print('')
        print(message)
        print("RTT: " + str(elapsed) + ' seconds')
    except timeout:
        # request doesn't return, prints timeout.
        print('')
        print(message)
        print("Request timed out.")
    #repeats until 20th packet is received.
    sequence_number = sequence_number +1

