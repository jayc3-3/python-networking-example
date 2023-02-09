#Import the socket module
import socket

#Create a class for networking
class Networking():
    #Define class variables
    DataToSend = ""
    RecievedDataStr = ""
    Client = ""
    ClientStr = ""

    #Create a inner function that will be ran on startup
    def __init__(self):
        #Define the host and port of the server
        self.ServerHost = "127.0.0.1"
        self.ServerPort = int(input("Input the server port: "))
        
        #Create the server
        self.Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        #Bind the server to the host and port
        self.Server.bind((self.ServerHost, self.ServerPort))

    #Create a inner function for recieving data
    def Recieve(self):
        try:
            #Wait for client to send data
            RecievedData, Networking.Client = self.Server.recvfrom(1024)
            
            #Convert the recieved data and the address of the client to a string
            Networking.RecievedDataStr = str(RecievedData, 'utf-8')
            Networking.ClientStr = str(Networking.Client)
        except:
            #Print a error message if the server fails to recieve data
            print("Error encountered when recieving data")
            quit()
    
    def Send(self, Data):
        try:
            #Attempt to send data to client with provided data
            self.Data = Data
            self.Server.sendto(self.Data.encode(), Networking.Client)
        except:
            #Print a error message if the server fails to send the data
            print("Error encountered when sending data")
            quit()