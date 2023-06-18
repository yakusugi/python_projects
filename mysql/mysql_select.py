import mysql.connector

store_name = str(input("What is the store name? "))

try:
    connection = mysql.connector.connect(host='localhost', 
                user='user', 
                password='pass', 
                database='db_name')

    cursor = connection.cursor(prepared=True)
    sql_query = """select * from sample_tbl where store_name = %s"""
    tuple1 = (store_name,)
    cursor.execute(sql_query, tuple1)

    for tbl in cursor:
        print(tbl)
   
    connection.commit()
    

except mysql.connector.Error as error:
    print("parameterized query failed {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")