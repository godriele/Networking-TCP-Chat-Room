import socket
import threading

# Choosing Nickname
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# ------- LIstening to Server and Sending Nicknames --------
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break 
        
# ------------ Sending Messages to Server --------------
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
        
# Starting Thead for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()