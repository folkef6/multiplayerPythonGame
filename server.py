import socket
from _thread import *
import pickle
from player import Player
from bullet import Bullet



server = "172.22.176.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
    
s.listen(2)
print("Waiting for a connection, Server Started")

players = [Player(0,0, 50, 50, (255,0,0), 5), Player(100, 100, 50, 50, (0,0,255), 5)]
bullets = []

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True: 
        try: 
            data = pickle.loads(conn.recv(2048))
            players[player] = data[0]
            bullets = data[1]
            
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else: 
                    reply = players[1]
                    
                #print("Received: ", data)
                #print("Sending: ", reply)
                
            
            conn.sendall(pickle.dumps((reply, bullets)))
        except:
            break    
            
    print("Lost connection ")
    conn.close()
    
current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    
    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
