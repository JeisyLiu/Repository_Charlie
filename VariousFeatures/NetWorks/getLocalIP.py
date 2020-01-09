import socket
hostname = socket.gethostname()
localIp = socket.gethostbyname(hostname)
print("my hostname is:", hostname)
print("my local ip address is:", localIp)