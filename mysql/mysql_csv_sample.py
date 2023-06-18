import csv
import mysql.connector

# Connect to the MySQL database
cnx = mysql.connector.connect(user='username', password='password', host='hostname', database='database_name')
cursor = cnx.cursor()

# Execute a SELECT clause to retrieve data from the database
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch the results and store them in a variable
results = cursor.fetchall()

# Close the cursor and connection
cursor.close()
cnx.close()

# Write the results to a CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['column1', 'column2', 'column3'])
    for row in results:
        writer.writerow(row)

print("Data exported successfully to output.csv")