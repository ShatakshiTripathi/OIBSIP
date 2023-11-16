import socket
import threading

def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{username}: {message}")
        except:
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))
server.listen(2)

print("Server listening on port")

clients = []

while len(clients) < 2:
    client_socket, _ = server.accept()
    username = client_socket.recv(1024).decode('utf-8')
    clients.append((username, client_socket))

    
    client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
    client_handler.start()

