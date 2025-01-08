import threading
'''
Will alows us work with threads, enabling us to run multiple tasks concurrently 
in a program. Threads are lightweight sub-processes that hsare the same memory space
'''
import socket
'''
Provides access to network communication using sockets, which allows us to send and 
receive data over the internet or a local network
'''
# Connection Data
host = '127.0.0.1' # Local Host
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET indicates that we are using an internet socket rather than a unix socket'
# SOCK_STREAM indicates that we are using TCP and not UDP 

server.bind((host, port))
server.listen()

# List For Clients and Their Nicknames
clients = []
ciknames = []

