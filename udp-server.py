import socket
import MySQLdb

class databaseInstance():
    def __init__(self):
        self.__host = "localhost"
        self.__user = "pythonuser"
        self.__password = "pythonpwd123"
        self.__database = "lab_users"
    
    def startConnenction(self):
        self.connection = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
    
    def checkAccessAndLog(self, card_id):
        thiscursor = self.connection.cursor()
        thiscursor.execute("SELECT username, access_to_lab FROM lab_users_labuser WHERE card_id = %(card_id)s", {'card_id': card_id})

        querydata = thiscursor.fetchone()
        if querydata:
            print("username:", querydata[0], "access_to_lab:", bool(querydata[1])) # For debug
            if querydata[1]: # If has access
                event_type = "Access Granted"
            else:
                event_type = "Access Denied"
        else:
            print("Unknown card_id:", card_id) # For debug
            event_type = "Unknown, Access Denied"

        thiscursor.execute("INSERT INTO lab_users.lab_users_event (card_id, event_type) VALUES(%(card_id)s, %(event_type)s)", {'card_id': card_id, 'event_type': event_type})
        self.connection.commit()
        thiscursor.close()
        if event_type == "Access Granted":
            return True
        else:
            return False

    def endConnection(self):
        self.connection.close()

database = databaseInstance()
database.startConnenction()

# bind all IP
HOST = '10.109.6.206'
# Listen on Port 
PORT = 35682 
#Size of receive buffer   
BUFFER_SIZE = 1024    
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the host and port
s.bind((HOST, PORT))
print("started listening")
while True:
    # Receive BUFFER_SIZE bytes data
    # data is a list with 2 elements
    # first is data
    #second is client address
    data = s.recvfrom(BUFFER_SIZE)
    if data:
        #print received data
        print('Client to Server: ' , data)
        # Convert to upper case and send back to Client
        access = database.checkAccessAndLog(data[1])
        s.sendto(data[0].upper(), access)
# Close connection
s.close()
