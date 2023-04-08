import socket

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostbyname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "End"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len (message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' '* (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send(f"client's IP address is {SERVER} and client's device name is {socket.gethostname()}" )
send(DISCONNECT_MESSAGE)