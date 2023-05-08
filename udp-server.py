import socket
import MySQLdb
import datetime

class databaseInstance():
    def __init__(self):
        self.__host = "localhost"
        self.__user = "pythonuser"
        self.__password = "pythonpwd123"
        self.__database = "lrl_database"
    
    def startConnenction(self):
        self.connection = MySQLdb.connect(self.__host, self.__user, self.__password, self.__database)
    
    def addUser(self, card_id):
        thiscursor = self.connection.cursor()
        thiscursor.execute("SELECT username FROM lab_users_labuser WHERE card_id = %(card_id)s", {'card_id': card_id})
        querydata = thiscursor.fetchone()
        if querydata:
            print("User already exists")
            return
        
        username = input("Enter username: ")
        year_grad = str(int(input("Enter graduation year: ")))
        now = datetime.datetime.now()
        isonow = now.strftime('%Y-%m-%d %H:%M:%S')
        thiscursor.execute("INSERT INTO lab_users_labuser (card_id, username, year_grad, access_to_lab, last_modified, date_added) VALUES (%s, %s, %s, 1, %s, %s)", (card_id, username, year_grad, isonow, isonow))
        self.connection.commit()
        thiscursor.close()
        return

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

        thiscursor.execute("INSERT INTO lrl_database.lab_users_event (card_id, event_type) VALUES(%(card_id)s, %(event_type)s)", {'card_id': card_id, 'event_type': event_type})
        self.connection.commit()
        thiscursor.close()
        if event_type == "Unknown, Access Denied":
            return b'A'
        if event_type == "Access Granted":
            return b'Y'
        else:
            return b'N'

    def endConnection(self):
        self.connection.close()

database = databaseInstance()
database.startConnenction()

HOST = '10.109.6.199'
PORT = 35682
BUFFER_SIZE = 255
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

database.addUser("b973aae2")
print("started listening")
while True:
    data, address = s.recvfrom(BUFFER_SIZE)
    print(data, address)
    if address:
        data = bytes(data).hex()
        print('Client to Server: ' , data, address)
        access = database.checkAccessAndLog(data)
        if access == b'A':
            database.addUser(data)
        else:
            s.sendto(access, address)
