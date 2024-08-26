import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Shubh@12",
    database = "mydatabase0"
)

mycursor = mydb.cursor()
sql = "DELETE FROM customers WHERE address = 'Highway 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) deleted")