import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Shubh@12",
    database = "mydatabase0"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = 'Highway 21'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)