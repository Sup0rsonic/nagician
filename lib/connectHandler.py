import socket
import sys
import time
import threading

host = socket.gethostbyname('localhost')
port = ''  # port
debug = True # debug options. There's NO bugs if you doesn't turn it on

conn = socket.socket(2, 1)

class connHandler():
    try:
        conn.bind((host,port))
    except Exception,e:
        print '[!]Failed to bind adddress(%s:%s),quitting.'
        if debug == True:
            print str(e)
        exit(1)

    def listen(self,conn): # Listen port
        pass

    def getRoute(self): # Get relay route
        pass

class listener(conn):
    def recv(self,buffer): # Recv buffer
        pass

class sender(conn):
    def send(self,buffer): # Send buffer
        pass

