import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# attempting connection with the server
client.connect(('localhost', 8888))

try:

    message = "Ping To Server!"

    # encoding to utf-8 byte format
    client.sendall(message.encode())

    recieved = 0
    total = len(message)

    while recieved != total:

        data = client.recv(16)

        recieved += len(data)

        print(f"Recieved {data.decode()}")

finally:

    client.close()