import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext
from zeroconf import Zeroconf, ServiceBrowser, ServiceStateChange
import errno
# Client configuration
PORT = 5555

# Create a Zeroconf instance for service discovery
zeroconf = Zeroconf()
discovery_finished = threading.Event()


# Tkinter GUI
class ChatGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("KindWords Chat")
        self.geometry("400x400")
        self.resizable(False, False)

        # Message Label
        self.msg_label = tk.Label(self, text="Messages:")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=0, pady=5)

        # Text area for displaying messages
        self.messages_area = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.messages_area.pack(expand=True, fill="both")
        self.messages_area.config(state='disabled')

        # Entry widget for typing messages
        self.message_entry = tk.Entry(self)
        self.message_entry.pack(expand=True, fill="x")

        # Button to send messages
        send_button = tk.Button(self, text="Send", command=self.send_message)
        send_button.pack()

        # Create a socket for the client
        self.client_socket = None
        self.connection_established = False

        #self.initialize_connection()

        if self.connection_established:
            # Receive and display the welcome message from the server
            un_message = self.client_socket.recv(1024).decode('utf-8')

            # Prompt user for username after displaying the welcome message
            usernames = un_message.split("\n")
            self.username = usernames[0]
            while self.username in usernames:
                self.username = simpledialog.askstring("Username", "Enter your username:")
            if not self.username:
                self.destroy()

            # Send Username to Server
            self.client_socket.sendall(self.username.encode('utf-8'))
            # Start a thread to receive messages
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()

            self.protocol("WM_DELETE_WINDOW", self.cleanup_and_exit)

            # Bind the Enter key to the send_message method
            self.message_entry.bind("<Return>", lambda event: self.send_message())



    def send_message(self):
        if not self.connection_established:
            return

        message = self.message_entry.get()
        if message:
            full_message = f"[{self.username}]: {message}"
            self.client_socket.sendall(full_message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                self.messages_area.config(state='normal')
                self.messages_area.insert(tk.END, message + "\n")
                self.messages_area.config(state='disabled')
                self.messages_area.yview(tk.END)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def cleanup_and_exit(self):
        # Cleanup logic, such as closing the socket
        if self.client_socket:
            self.client_socket.close()
        self.destroy()  # Close the Tkinter window



# Function to connect to the discovered server
def connect_to_server(chat_gui, server_ip):
    try:
        # Create a socket for the client
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, PORT))
        chat_gui.client_socket = client_socket
        chat_gui.connection_established = True
    except Exception as e:
        print(f"Error connecting to server: {e}")
        chat_gui.connection_established = False


# Callback function when a service is discovered
def on_service_state_change(zeroconf, service_type, name, state_change):
    if state_change is ServiceStateChange.Added:
        info = zeroconf.get_service_info(service_type, name)
        if info:
            addresses = info.parsed_addresses()
            if addresses:
                # Convert the string address to bytes
                address_bytes = bytes(map(int, addresses[0].split('.')))
                server_ip = socket.inet_ntoa(address_bytes)
                print(f"Discovered server at {server_ip}")
                chat_gui.after(0, lambda: connect_to_server(chat_gui, server_ip))

    discovery_finished.set()


# Browse for services of type "_chat._tcp.local."
browser = ServiceBrowser(zeroconf, "_chat._tcp.local.", handlers=[on_service_state_change])

# Create an instance of the ChatGUI class
chat_gui = ChatGUI()

# Tkinter main loop
chat_gui.mainloop()

discovery_finished.wait()
zeroconf.close()
print("FIN")
