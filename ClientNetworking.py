#Import modules
import socket

#Define "Networking" class
class Networking:
    #Define class variables
    DataToSend = ""
    RecievedData = ""
    RecievedDataStr = ""
    
    def __init__(self):
        #Setup client
        self.Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ServerAddress = "127.0.0.1"
        self.ServerPort = 10957
        self.Server = (self.ServerAddress, self.ServerPort)
        
    def Connect(self):
        #Attempt connection to server
        try:
            self.Client.connect(self.Server)
        except:
            pass
    
    def Send(self):
        #Attempt to send data to server
        try:
            self.Client.sendto(Networking.DataToSend.encode(), self.Server)
        except:
            pass
    
    def WaitForData(self):
        #Wait for data to be sent from server
        RecievedData, Server = self.Client.recvfrom(1024)
        Networking.RecievedDataStr = str(RecievedData, 'utf-8')