import socket

target_host = "www.google.com"
target_port = 80

#CREAT A SOCKET OBJECT 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#CONNECT THE CLIENT AND THE HOST 
client.connect((target_host,target_port))

#SEND SOME DATA 
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#RECEIVE SOME DATA 
response = client.recv(4096)

#PRINT RESPONSE 
print(response)