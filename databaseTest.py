import mysql.connector

conn = mysql.connector.connect(username='root', password='Azsxdc!#312',host='127.0.0.1',database='fcdetect',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()