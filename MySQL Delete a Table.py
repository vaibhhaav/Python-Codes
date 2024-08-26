import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Shubh@12",
    database = "mydatabase0"
)

mycursor = mydb.cursor()
sql = "DROP TABLE customers"
mycursor.execute(sql)