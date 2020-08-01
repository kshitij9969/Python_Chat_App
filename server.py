import socket
from _thread import *
import threading

HOST = '127.0.0.1'
PORT = 65432

print_lock = threading.Lock()


def connect_to_client(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            print_lock.release()
            break
        conn.sendall(data)
    conn.close()


def main():
    global HOST
    global PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print("Host is binded to the port: " + str(PORT))
    s.listen(5)
    print("Socket is listening")
    while(1):
        c, addr = s.accept()
        print_lock.acquire()
        print("Connected to " , addr[0] , ":" , addr[1])
        start_new_thread(connect_to_client, (c,))
    s.close()


if __name__=="__main__":
    main()