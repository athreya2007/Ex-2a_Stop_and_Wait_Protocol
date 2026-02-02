import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345  ))
print("Connected to server")

while True:
    recvie = client_socket.recv(1024).decode()
    if recvie == "Exit":
        break

    print("Server:", recvie)
    message = "Client says:ACK sent"
    client_socket.send(message.encode())
client_socket.close()
