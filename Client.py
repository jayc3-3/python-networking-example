#Import the "Networking" class from ClientNetworking.py
from ClientNetworking import Networking

#Setup networking
Net = Networking()
Net.Connect()
Net.DataToSend = "Test!"

#Send data to server
Net.Send()

#Wait for response from server
Net.WaitForData()

#Print response from server
print("Data recieved: " + Net.RecievedDataStr)