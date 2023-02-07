#from fastapi import FastAPI, Path, Query
#import uvicorn
import mysql.connector

def CheckAdmin(Name, Password):
    cursor = conn.cursor()
    query = "SELECT AdminPassword FROM lrldb.lietotaji WHERE LietotajaNickname =" + Name
    cursor.execute(query)
    result = cursor.fetchall()
    if not result:
        return False
    else:
        if(str(result[0][0]) == Password):
            return True
        else:
            return False

def User(LietotajaID):
    if(int(LietotajaID)>-1):
        cursor = conn.cursor()
        query = "SELECT * FROM lrldb.lietotaji WHERE LietotajaID =" + LietotajaID
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print(x)
        cursor.close()
    else:
        print("id neeksistē")
def ChangeAccess(LietotajaID, Access):
    cursor = conn.cursor()
    value = (Access, LietotajaID)
    query = "UPDATE lrldb.lietotaji SET Access = %s WHERE LietotajaID = %s"
    cursor.execute(query, value)
    conn.commit()
    cursor.close()

def CheckAccess(LietotajaID):
    cursor = conn.cursor()
    query = "SELECT Access FROM lrldb.lietotaji WHERE LietotajaID =" + LietotajaID
    cursor.execute(query)
    result = cursor.fetchall()
    x = result[0][0]
    cursor.close()
    print(x)
    return x

def AllUsers():
    cursor = conn.cursor()
    query = "SELECT * FROM lrldb.lietotaji"
    cursor.execute(query)
    result = cursor.fetchall()
    for x in result:
        print(x)
    cursor.close()

Select = 1

while 0 < Select:
    print("Iechecko cilveku(1)")
    print("Maini access(2)")
    print("Iechecko cilveka access(3)")
    print("Iechecko visus cilvekus(4)")

    try:
        conn = mysql.connector.connect(user='davisstrazds', password='b9xVf4JZ', host='10.109.6.70',
                                       database='lrldb')
        Select = int(input("funkcija:"))
    except:
        print("connection error")
        Select = 0

    if(Select == 1):
        Name = "'" + input("name:" ) + "'"
        Password = input("Password:")
        if(CheckAdmin(Name, Password) == True):
            LietotajaID = input("id:")
            User(LietotajaID)
        else:
            print("Admins ir invalids")
    elif(Select == 2):
        Name = "'" + input("name:" ) + "'"
        Password = input("Password:")
        if(CheckAdmin(Name, Password) == True):
            LietotajaID = input("id:")
            Access = int(input("Access:"))
            ChangeAccess(LietotajaID, Access)
        else:
            print("Admins ir invalids")
    elif(Select==3):
        Name = "'" + input("name:" ) + "'"
        Password = input("Password:")
        if(CheckAdmin(Name, Password) == True):
            LietotajaID = input("id:")
            CheckAccess(LietotajaID)
        else:
            print("Admins ir invalids")
    elif(Select==4):
        Name = "'" + input("name:" ) + "'"
        Password = input("Password:")
        if(CheckAdmin(Name, Password) == True):
            AllUsers()
        else:
            print("Admins ir invalids")
#app = FastAPI()

#@app.post("/get_person")


#if __name__ == "__main__":
#    uvicorn.run(app, host="10.109.6.67")