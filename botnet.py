import socket

servaddr = ''
servport = ''
debug = True

if debug == True:
    servaddr = '127.0.0.1'
    servport = 23335

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.bind((servaddr, servport))
    if debug == True:  # SIMULATE_BOT
        print '[#]500 debug bot generate'
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #bot.connect((servaddr, servport))
        try:
            while True:
                connect,address = client.accept()
                response = client.recv(1024)
                print response
        except Exception,E:
                client.close()
                bot.close()
                print E

except Exception, E:
    print '[!]Falied to load botnet handler'
    print E