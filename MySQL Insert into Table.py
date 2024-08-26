import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Shubh@12",
    database = "mydatabase0"
)

mycursor = mydb.cursor()
sql = "INSERT INTO customers (name,address) VALUES (%s,%s)"
val = ("John","Highway 21")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")