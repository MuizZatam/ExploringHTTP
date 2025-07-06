import socket

# Creating a socket object:

# The following loc creates a socket that uses INET (IPV4) Address Family
# This means that the server is bound to communicate with IPV4 addresses

# Socket Types (https://www.ibm.com/docs/pl/aix/7.1.0?topic=protocols-socket-types)
# The SOCK_STREAM Socket type:
# 1. Provides 2 way communication - Data can flow in both directions simultaneously
# over an established connection
# 2. Ensures reliable data transmission over TCP
# 3. Transmits data Sequentially and as a stream
# 4. Guarantees Error checking and correction
# 5. Common Protocols like HTTP, FTP, etc. utilize this Socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the server to a URL (localhost) and a port
# A URL is to identify where the server is, a port is to identify which process should recieve
# the request

server.bind(('localhost', 8888))

# NOTE: How does a browser realize what port to send the request to?

# The server continuously listens for incoming requests
# The backlog param (set to 1) defines the max number of pending requests 
# that the OS can queue for accepting before it starts rejecting new ones
# In this case, if a server recieves more than 1 request before it responds to
# the first request, it drops the connection for later requests altogether
# This doesn't mean that the server can only handle one connection,
# it just limits how many can be waiting in line at once.

server.listen(1)

# This loop keeps listening till a request is accepted

while True:

    print("Listening to Incoming Requests")
    
    # The connection object is the actual TCP connection formed
    # (See connection oriented vs connectionless)
    # The client address is the IP of requesting client
    connection, client_address = server.accept()

    break

print(f"Connection Accepted From {client_address}")

# Note: using try-finally for if an exception occurs, the connection is closed properly
try:

    while True:

        # Accepts data upto 16 bytes at a time
        # If data greater than 16 bytes is recieved,
        # remaining data is stored in socket buffer of the server
        # and is recieved subsequently
        data = connection.recv(16)

        if data:

            print(f"Acquired Data: {data}, Echoing back to client")

            # Sendall ensures that all provided data is sent (Pythonic)
            # send is a lower level implementation that may not always send
            # all data due to transmission errors
            # sendall automatically retransmits pending data
            # whereas send requires manual logic for this. (Do check out how this works!)
            connection.sendall(data)

        else:

            print("No more data from Client")

            break

finally:

    connection.close()