#Import "Networking" class from ServerNetworking.py
from ServerNetworking import Networking

#Define shorter name for "Networking" class
Net = Networking()

#Wait for data from client
Net.Recieve()

#Print recieved data from client, as well as the address it was send from
print("Data recieved from client: " + Net.RecievedDataStr)
print("Address of client who sent data: " + Net.ClientStr)

#Send response to client
Net.DataToSend = input("Data to send to client: ")
Net.Send(Net.DataToSend)
