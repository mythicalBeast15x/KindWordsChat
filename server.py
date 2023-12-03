import socket
import threading
from zeroconf import Zeroconf, ServiceInfo
from generateHash import load_hash, HashTable
# Server configuration
#HOST = '127.0.0.1'
#HOST = '0.0.0.0'
PORT = 5555

'''
# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
'''
# Get the local IP address
local_ip = socket.gethostbyname(socket.gethostname())

# Convert the PORT variable to an integer
PORT = int(PORT)
hash_table = load_hash('profanities.pkl')


def filter_message(msg, hash):
    words = msg.split(' ')
    name = words.pop(0)
    new_msg = name
    for word in words:
        if hash.check_word(word):
            word = "*"*len(word)
        new_msg += " " + word
    new_msg = new_msg

    return new_msg

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((local_ip, PORT))
server_socket.listen()

# Create a Zeroconf service to advertise the server
zeroconf = Zeroconf()
service_info = ServiceInfo(
    type_="_chat._tcp.local.",
    name=f"ChatServer._chat._tcp.local.",
    server=f"{socket.gethostname()}.local.",
    port=PORT,
    weight=0,
    priority=0,
    properties={},
)
zeroconf.register_service(service_info)



# List to keep track of connected clients
clients = []
usernames = []


# Function to handle a client's connection
def handle_client(client_socket, client_address):
    # Send Users
    user_string = "root"
    for user in usernames:
        user_string = user_string + "\n" + user

    # Send Usernames to client
    client_socket.sendall(user_string.encode('utf-8'))

    # Receive Username and Update List of Usernames
    username = client_socket.recv(1024).decode('utf-8')
    usernames.append(username)
    welcome = "Successfully Connected!\n"
    client_socket.sendall(welcome.encode('utf-8'))
    message = f"{username} has joined the Chat!"
    for c in clients:
        c.sendall(message.encode('utf-8'))

    print(f"Connection established with {client_address}:[{username}]")

    while True:
        try:
            # Receive and broadcast messages
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Filter message
            message = filter_message(message, hash_table)

            print(f"Received message from {client_address}: {message}")

            # Broadcast the message to all connected clients

            for c in clients:
                c.sendall(message.encode('utf-8'))

        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break

    # Remove the client from the list if disconnected
    index = clients.index(client_socket)
    username = usernames.pop(index)

    clients.remove(client_socket)
    client_socket.close()
    user_disconnect_msg = f"{username} has disconnected."
    for c in clients:
        c.sendall(user_disconnect_msg.encode('utf-8'))
    print(f"Connection closed with {client_address}")

# Accept incoming connections
print(f"Server listening on {local_ip}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    # Create a thread to handle the new client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()