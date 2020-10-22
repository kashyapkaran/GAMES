import socket
from _thread import *
import sys

server = "192.168.1.6"

port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#the number in this bottom line of code is = the number of plaoyers

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for connection, Server Started...")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


pos = [(0, 0), (100, 100)]


def threaded_client(conn,player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

                        
            if not data:
                print("Disconnected")
                break
            
            else:
                if player == 1:
                    reply = pos[0]
                
                else:
                    reply = pos[1]
                print("received: ", data)
                print("sending: ", reply)
                
            conn.sendall(str.encode(make_pos(reply)))
            
        except:
            break
        
        print("lost connection")
        conn.close()


currentPlayer = 0


while True:
    conn, addr = s.accept()
    print("Connected to :", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    #a= input("Press any key")




