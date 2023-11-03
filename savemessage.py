#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import cgitb
import mysql.connector

# Enable CGI traceback for debugging (remove in production)
cgitb.enable()

# Connect to the MySQL database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Get the form data from the CGI request
form = cgi.FieldStorage()

# Get the values from the form fields
sender = form.getvalue('sender')
recipient = form.getvalue('recipient')
message = form.getvalue('message')

# Save the message in the database
sql = "INSERT INTO messages (sender, recipient, message) VALUES (%s, %s, %s)"
values = (sender, recipient, message)
cursor.execute(sql, values)
db.commit()

# Fetch the saved message from the database
message_id = cursor.lastrowid
select_sql = "SELECT * FROM messages WHERE id = %s"
select_values = (message_id,)
cursor.execute(select_sql, select_values)
result = cursor.fetchone()

# Close the database connection
db.close()

# Print the HTTP response
print("Content-Type: text/html")
print()
# Print the success message
print("Message sent!")
