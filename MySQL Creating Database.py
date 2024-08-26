import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Shubh@12"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase0")