import socket

target_host = "172.20.10.3"
target_port = 80

#CREATE A SOCKET OBJECT 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#CONNECT THE CLIENT AND THE HOST 
client.connect((target_host,target_port))

#SEND SOME DATA 
#message = "GET / HTTP/1.1\r\n Host: cn.bing.com\r\n\r\n"
message = "ABCDEF"
client.send(message.encode())

#RECEIVE SOME DATA 
response = client.recv(4096)

#PRINT RESPONSE 
print(response)