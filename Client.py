import socket
import threading

def receive_messages(client_socket):
    while True:
        # Receive data from the server
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break 

        print(f"Received from server: {data}")

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        client_msg = input("User 1: ")
        client.send(client_msg.encode('utf-8'))

if __name__ == "__main__":
    start_client()
