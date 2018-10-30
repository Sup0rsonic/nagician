import pickle
import socket

class server():

    ip = socket.gethostbyname(socket.gethostname())
    port = 1444

    def codegen(self,file,*code):
        try:
            raw = open(file,'r')
        except:
            print '[!]500'

    def listenu(self):
        usocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        usocket.bind((self.ip,self.port))
        pass

    def listent(self,port):
        pass

    def sendcode(self,ip,port):
        pass

    def sendcmd(self,ip,port,cmd):
        pass
