import mysql.connector
my_conn = mysql.connector.connect(host="localhost", user="user", password="pass")
print(my_conn);
