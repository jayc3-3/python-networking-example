#Import the "Networking" class from ClientNetworking.py
from ClientNetworking import Networking

#Define a shorter name for the class
Net = Networking()

#Connect to the server
Net.Connect()

#Send data to server
Net.DataToSend = input("Data to send to server: ")
Net.Send(Net.DataToSend)

#Wait for data from server
Net.WaitForData()

#Print recieved data from server
print("Data recieved from server: " + Net.RecievedDataStr)
