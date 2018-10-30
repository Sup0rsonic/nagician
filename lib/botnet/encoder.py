import hashlib
import base64
import struct
import gzip
import binascii


# I'm really sick of this sh*t.
# F**K THE ENCODING -- or my code?
# This will be the final version - at least there's no bugs.

# Preset
host = '' # C2 host addr
psk = '' # PSK
custom_num = '' # Custom number for cipher

debug = True # debug options

if debug == True:
    host = '233.233.233.233'
    psk = 'thisispsk'
    custom_num = '2'

def cipher_gen(host):
    key = int(custom_num)
    cipher_raw = str(host)
    buf = ''
    for i in cipher_raw:
        buf += str(ord(i))
    if len(buf) <= 75:
        buf = buf.rjust(72 , custom_num)
    buf = int(buf)
    buf = str(buf)
    c1 = buf[0:24]
    c2 = buf[25:51]
    c3 = buf[52:]
    c1 = int(c1) ^ str2int(psk)
    c2 = int(c2) ^ str2int(psk)
    c3 = int(c3) ^ str2int(psk)
    register = c1
    c1 = c2 ^ key
    c2 = c3 ^ key
    c3 = register ^ key
    cipher = str(c1) + str(c2) + str(c3)
    cipher = int(cipher)
    return cipher

def encrypt(raw):
    raw = str(raw)
    if len(raw) <= 120:
        raw = raw.ljust(120,custom_num)
    buf = str2hex(raw) # hexified string
    cipher = cipher_gen(host)
    buf = int(buf) ^ cipher
    c0 = str(buf)[0:80] # 80?
    c1 = str(buf)[80:160] # 81-161
    c2 = str(buf)[160:] # 162-240
    tmp = int(c0) ^ cipher # 81
    c0 = int(c1) ^ cipher # 81
    c1 = int(c2) ^ cipher # 81
    buf = str(c0) + str(c1) + str(tmp)
    buf = str2hex(str(buf))
    hash = hashlib.md5(buf).hexdigest()
    buf += hash
    sum = str(len(buf)).ljust(4,custom_num)
    buf += sum

    return buf

def decrypt(raw,mode='HARD'):
    sum = raw[-4:].rstrip(custom_num)
    hash = raw[-36:-4]
    buf = raw[:-36]
    if int(sum) != len(buf + hash):
        print 'ERR'
    if hash != hashlib.md5(buf).hexdigest():
        print 'ERR'
    buf = hex2str(buf)
    cipher = cipher_gen(host)
    c0 = int(buf[-81:]) ^ cipher
    c1 = int(buf[0:81]) ^ cipher
    c2 = int(buf[81:162]) ^ cipher
    buf = str(c0) + str(c1) + str(c2)
    buf = int(buf) ^ cipher
    buf = hex2str(buf)
    raw = buf.rstrip(custom_num)
    return raw

def str2hex(cipher):
    buf = cipher.encode('hex')
    return buf

def hex2str(cipher):
    buf = str(cipher).decode('hex')
    return buf

def int2str(cipher):
    buf = ''
    for i in range(0,len(str(cipher)),2):
        tmp = cipher[i]
        tmp += cipher[i+1]
        buf += chr(int(tmp))
    return buf

def str2int(cipher):
    buf = ''
    for i in range(0,len(cipher)):
        buf += str(ord(cipher[i]))
    return int(buf)
