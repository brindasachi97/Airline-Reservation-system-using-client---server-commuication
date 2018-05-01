import socket 
from SocketServer import ThreadingMixIn 
from clientthread import ClientThread
import json
#from db import insert
#from db import print_all

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = "127.0.0.1"
TCP_PORT = input("Port: ")

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
tcpServer.listen(4)
threads = [] 

print "Multithreaded Python server : Waiting for connections from TCP clients..."

while True: 
    (conn, addr) = tcpServer.accept()
    newthread = ClientThread(conn,addr) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join()

