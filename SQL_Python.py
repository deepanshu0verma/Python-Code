import pymysql

connection = pymysql.connect(
    user="toor", passwd="Toor@123", host="localhost", port=3306, database="mydb"
)
cursor = connection.cursor()
selectquery = "SELECT * FROM Doctors"
cursor.execute(selectquery)
res = cursor.fetchall()
print(res)


cursor.close()
connection.close()
