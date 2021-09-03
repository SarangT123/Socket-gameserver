import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "?DISCONNECT"

# setting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)  # setting the addres

users = []


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected to the server")
    connected = True
    users.append(conn)
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # getting the msg length
        # checking if its a valid message send by the client(Not the joining message)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)  # dedoding the msg
            if msg == DISCONNECT_MESSAGE:
                connected = False  # disconnecting id var disconnect message recived
            print(f"[{addr}] {msg}")
            conn.send("Message recived".encode(FORMAT))  # Returning a message
            at = conn
            for i in range(len(users)):
                conn = users[i]
                conn.send(f"Message recived {msg}".encode(FORMAT))
    conn.close()  # closing the connection


def start():
    server.listen()  # listening to conections
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(
            conn, addr))  # creating a new thread for that user
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print(f"Server starting at\n host: {SERVER} \n port: {PORT}")
start()  # starting the server
