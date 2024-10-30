import socket
import threading
from cryptography.fernet import Fernet # type: ignore

# Symmetric encryption key (should be securely shared between server and clients)
# This should be generated once and securely shared with clients.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

clients = []

# Function to broadcast a message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle client connections
def handle_client(client):
    while True:
        try:
            # Receive encrypted message from client
            encrypted_message = client.recv(1024)
            if encrypted_message:
                # Decrypt the message
                decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
                print(f"Received and decrypted message: {decrypted_message}")
                # Re-encrypt and broadcast it to other clients
                broadcast(cipher_suite.encrypt(decrypted_message.encode()))
        except Exception as e:
            print(f"Error: {e}")
            clients.remove(client)
            client.close()
            break

# Main server loop to accept connections
def start_server():
    print(f"Server is listening... Encryption key: {key.decode()}")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

start_server()
