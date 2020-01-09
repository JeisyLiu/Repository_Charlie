import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        

print("Waiting for client's requirement")
s.listen(5)                 
for i in range(5):
   c, addr = s.accept()     
   print("Got connection from")
   print(addr)
   c.send(b"Thanks for connecting")
   c.close()                