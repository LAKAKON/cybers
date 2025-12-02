import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5500))
s.listen()

clients = []
chat = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def handle_clients(conversation, info):
    clients.append(conversation)
    username = ""
    while True:
        message = conversation.recv(1024).decode()
        if message.startswith("Username: "):
            username = message[10:]
            conversation.send("Welcome to server!".encode())
            continue
        global chat
        message = (username + ": " + message)
        broadcast(message, conversation)
        if message == "Bye":
            broadcast(f"{username} has disconnected.", conversation)
            conversation.send("You have disconnected.".encode())
            break
while True:
        conn, addr = s.accept()
        client_thread = threading.Thread(target=handle_clients, args=(conn, addr), daemon=True)
        client_thread.start()