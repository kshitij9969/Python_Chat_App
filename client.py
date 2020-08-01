import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Enter the message(whatever you enter, you will receive back from the server:')
    message = input()
    s.sendall(bytes(message, 'utf-8'))
    data = s.recv(1024)
    print("received", repr(data))
