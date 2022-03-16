import imp
import socket
from _thread import *
import sys
from game import Game
import pickle

server = "192.168.29.21"
port = 5555

# Lets us connect through IPv4 address
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))  # Allows connection through the port

except socket.error as e:
    str(e)

# opens up the port to allow connections (2 people, if no input unlimited)
s.listen(2)
print("Waiting for connection, Server Started")

snake_pos1 = [100, 50]
snake_pos2 = [200, 300]
games = [Game(snake_pos1), Game(snake_pos2)]


def threaded_client(conn, game):
    conn.send(pickle.dumps(games[game]))  # Sends the initial position on connect

    reply = ""
    while True:
        try:
            # Size of the data received, increase value with 2048*2, if error
            data = pickle.loads(conn.recv(2048))
            games[game] = data

            if not data:  # IF no data received, stop loop
                print("Disconnected")
                break
            else:
                if game == 1:
                    reply = games[0]
                else:
                    reply = games[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:  # Keeps looking for connections
    # Will accept any connection and store object in conn and address in addr
    conn, addr = s.accept()
    print("Connected to:", addr)

    # Allows the function to run along with the while loop still running the same time
    # Otherwise the while loop would have to wait for the function to finish
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
