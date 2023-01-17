import mysql.connector

conn = mysql.connector.connect(
    host="", #jaieliek ip no SQL hosta
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
#ja izprinte SQL versiju viss strada
