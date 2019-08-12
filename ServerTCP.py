import socket
import threading

bind_ip = "172.20.10.3"
bind_port = 80

#CREATE A SERVER 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#SPECIFY THE IP AND PORT THAT THE SERVER WILL LISTEN ON
server.bind((bind_ip,bind_port))

#MAXIMUM BACKLOG OF CONNECTIONS SET TO 5
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip,bind_port))

#CLIENT HANDLING THREAD
def HandleClient(client_socket):

    #print out what client requested
    request = client_socket.recv(1024)
    print("[*] Received: %s" % request)

    #send back a pkt
    re_message = "ACK"
    client_socket.send(re_message.encode())

    client_socket.close()

while True:
    [client,addr] = server.accept()
    print("[*] Accepting connections from: %s:%d" % (addr[0],addr[1]))

    client_handler = threading.Thread(target = HandleClient,args=(client,))
    client_handler.start()