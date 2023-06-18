import mysql.connector
my_conn = mysql.connector.connect(host="localhost", user="user", password="pass")
cur = my_conn.cursor()
cur.execute("show databases")

for db in cur:
    print(db)
