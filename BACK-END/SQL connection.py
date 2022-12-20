import mysql.connector

conn = mysql.connector.connect(
    host="192.168.238.131",
    user="davisstrazds",
    password="b9xVf4JZ",
    database="lrldb"
)
cursor = conn.cursor()
cursor.execute("DESCRIBE lietotaji")
version = cursor.fetchall()
print("MySQL version:", version)
cursor.close()
conn.close()


