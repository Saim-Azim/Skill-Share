#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector

# Get the username, sender, and reply from the query parameters
query_string = cgi.FieldStorage()
username = query_string.getvalue('uname')
sender = query_string.getvalue('sender')
reply = query_string.getvalue('reply')

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sum@iy@27",
    database="skillshare"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Define the SQL query to insert the reply message into the database
sql = "INSERT INTO messages (sender, recipient, message) VALUES (%s, %s, %s)"
params = (username, sender, reply)

# Execute the SQL query
cursor.execute(sql, params)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()

# Set the response headers
print("Content-type: text/plain")
print()

# Send a success message
print("Reply sent to", sender)
