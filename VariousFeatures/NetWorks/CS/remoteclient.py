import socket               
import sys

if len(sys.argv) < 2:
    print("please input target server ip address after cmd line")
s = socket.socket()
port = 12345       
try:         
    s.connect((sys.argv[1], port))
except ConnectionError:
    print('there is no such a server')
    exit(0)
print(s.recv(1024)) 
s.close()  