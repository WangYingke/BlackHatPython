import socket

target_host = "127.0.0.1"
target_port = 80

#CREATE A SOCKET OBJECT 
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#SEND SOME DATA 
client.sendto("AAABBBCCC",(target_host,target_port))

#RECEIVE SOME DATA
[data,addr]=client.recvfrom(4096)

#PRINT DATA 
print(data)