# Networking-TCP-Chat-Room
Credits to NeuralNine

Commit
COmmit 
Commit

This project is a simple real-time chat application where multiple clients can connect to a server and exchange messages. It uses Python's socket and threading modules for network communication and concurrent processing.

## Features
Server:
Listens for and accepts multiple client connections.
Broadcasts messages to all connected clients.
Handles client disconnections.

Client:
Connects to the server and chooses a nickname.
Sends and receives messages to/from the server.
Displays messages from other clients in real-time.

## Technologies
Python: Uses socket and threading for network communication and concurrency.
TCP Sockets: Communication between server and client is via TCP (SOCK_STREAM).
Threading: Handles multiple clients concurrently.

### Setup
Clone or download the repository.
- Run the server:
`python server.py`

- Run the client:
`python client.py`

Enter a nickname when prompted to connect.

## Usage
Clients can send messages to each other, and all connected clients will receive them.
If a client disconnects, others are notified.
### Example
Server:
Server is listening.....
Client prompts for nickname:

Choose your nickname: Alice

Chat:
Alice: Hello Bob!

Bob: Hi Alice!

Disconnection:
Alice left the chat!
