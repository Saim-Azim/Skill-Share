#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sum@iy@27",
    database="skillshare"
)

# Get the form data (username and event title)
form = cgi.FieldStorage()
username = form.getvalue('uname')
title = form.getvalue('title')

# Delete the event from MySQL
cursor = db.cursor()
delete_query = "DELETE FROM events WHERE sender = %s AND title = %s"
cursor.execute(delete_query, (username, title))
db.commit()

# Close the database connection
db.close()

# Set the response headers
print("Content-Type: text/plain")
print()

# Print a success message
print("Event deleted successfully")
