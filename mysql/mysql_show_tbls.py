import mysql.connector
my_conn = mysql.connector.connect(host="localhost", user="user", password="pass", database="db_name")
cur = my_conn.cursor()
cur.execute("show tables")

for tbl in cur:
    print(tbl)
