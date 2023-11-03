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
title = form.getvalue('title')
receiver = form.getvalue('receiver')
date = form.getvalue('e_date')
time = form.getvalue('e_time')
sender = form.getvalue('sender')

# Check if the request data already exists in the events table
sql = "SELECT * FROM events WHERE title = %s AND receiver = %s AND sender = %s"
values = (title, receiver, sender)
cursor.execute(sql, values)
result = cursor.fetchone()

# Print the HTTP response
print("Content-Type: text/plain")
print()

# Check if the request data exists
if result is not None:
    print("Request already sent!")
else:
    # Save the request in the database
    sql = "INSERT INTO events (title, receiver, e_date, e_time, sender) VALUES (%s, %s, %s, %s, %s)"
    values = (title, receiver, date, time, sender)
    cursor.execute(sql, values)
    db.commit()
    print("Request sent successfully!")

# Close the database connection
db.close()