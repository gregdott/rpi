# Originally taken from https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
# Minor modifications have been done (if any at all)

import socket
import os
from dotenv import load_dotenv

load_dotenv()

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    host = os.getenv('HOST_IP')
    
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    #message = input(" -> ")  # take input

    #while message.lower().strip() != 'bye':
    while True:
        #client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()