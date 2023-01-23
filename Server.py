#Import modules
import socket

#Setup server
ServerHost = "127.0.0.1"
ServerPort = 10957
Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Server.bind((ServerHost, ServerPort))

#Wait for client to send data
RecievedData, ClientAddr = Server.recvfrom(1024)
RecievedDataStr = str(RecievedData, 'utf-8')
ClientAddrStr = str(ClientAddr)

#Print the recieved data from the client
print("Data recieved from client: " + RecievedDataStr)
print("Address of client who sent data: " + ClientAddrStr)

#Send response message to client
DataToSend = "Hello Client!"
Server.sendto(DataToSend.encode(), ClientAddr)