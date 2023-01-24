#Import the "Networking" class from ClientNetworking.py
from ClientNetworking import Networking

#Setup networking
Net = Networking()
Net.Connect()
Net.DataToSend = "Hello server!"

#Send data to server
Net.Send(Net.DataToSend)

#Wait for response from server
Net.WaitForData()

#Print response from server
print("Data recieved: " + Net.RecievedDataStr)
