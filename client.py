import random
import socket
import keyboard
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "?DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(msg)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


while True:
    if keyboard.is_pressed('q'):
        send(
            f"player coords : x={random.randint(1,1000)} , y={random.randint(1,1000)}")
    elif keyboard.is_pressed('j'):
        send(DISCONNECT_MESSAGE)
        break

send(DISCONNECT_MESSAGE)
