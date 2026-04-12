import random
import socket
import time

import client
server  =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",9999))
while True:
    message,client_source = server.recvfrom(1024)
    number =  random.randint(1,10)
    if number ==1:
        continue
    if number == 2:
        time.sleep(5)
        server.sendto("hello client ".encode("utf-8"),client_source) 
    else:
        server.sendto("hello client ".encode("utf-8"),client_source) 

    print(message.decode('utf-8'))
    