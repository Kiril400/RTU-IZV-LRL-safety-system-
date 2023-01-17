import mysql.connector

id= "'" + input("id:") + "'" #ievada LietotajaID

conn = mysql.connector.connect(
    host="", #SQL host ip
    user="davisstrazds",
    password="b9xVf4JZ",
    database="lrldb"
)
cursor = conn.cursor()
query = "SELECT * FROM lrldb.lietotaji WHERE LietotajaID=" + id

cursor.execute(query)

result = cursor.fetchall()

for x in result:
    print(x)     #izprinte cilveka access statusu (0 vai 1)

cursor.close()
