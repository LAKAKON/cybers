import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 5500))
username = input("Enter your username: ")
username = "Username: " + username
client.send(username.encode())
content = client.recv(1024).decode()
print(content)


def Listen(client):
    while True:
        content = client.recv(1024).decode()
        print(content)
        if content.startswith("You have disconnected"):
            raise ConnectionError("You have disconnected.")

client_thread1 = threading.Thread(target=Listen, args=(client,))
client_thread1.start()

print("Enter your message: ")
while True:
    message = input().encode()
    client.send(message)