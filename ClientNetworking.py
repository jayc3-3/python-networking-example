#Import socket module
import socket

#Create class for networking
class Networking():
    #Define class variables
    DataToSend = ""
    RecievedData = ""
    RecievedDataStr = ""
    
    #Create a inner function that is ran on startup
    def __init__(self):
        #Create a client socket
        self.Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        #Set the time out for recieving data from server
        self.Client.settimeout(10)
        
        #Set the server address and port
        self.ServerAddress = input("Input the address of the server: ")
        self.ServerPort = int(input("Input the port of the server: "))
        
        #Define shorter name for server
        self.Server = (self.ServerAddress, self.ServerPort)

    #Create a inner function to connect to the server
    def Connect(self):
        #Attempt a connection to the server when .Connect() is called
        try:
            #Attempt to connect to the server
            self.Client.connect(self.Server)
        except:
            #Print if connection fails
            print("Ecountered an error while connecting to server")
            quit()
    
    #Create a inner function for sending data to server
    def Send(self, Data):
        #Attempt to send data when .Send() is called
        try:
            #Attempt to send data
            self.Data = Data
            self.Client.sendto(self.Data.encode(), self.Server)
        except:
            #Print message if sending data fails
            print("Ecountered an error while sending data")
            quit()

    #Create a inner function to wait for data from server
    def WaitForData(self):
        #Wait for data from server when .WaitForData() is called
        try:
            #Wait for data from server
            RecievedData, Server = self.Client.recvfrom(1024)
            del(Server)
            Networking.RecievedDataStr = str(RecievedData, 'utf-8')
        except:
            #Print error message if the connection times out
            print("Encountered an error while waiting for data")
            quit()
