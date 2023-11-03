#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import json
import mysql.connector

# Get the username from the query parameter
query_string = cgi.FieldStorage()
username = query_string.getvalue('uname')

# Establish a connection to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sum@iy@27",
    database="skillshare"
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Define the SQL query to fetch the user's message inbox data
sql = "SELECT * FROM messages WHERE recipient = %s"
params = (username,)

# Execute the SQL query
cursor.execute(sql, params)

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Close the database connection
db.close()

# Prepare the response data
messages = []
for row in rows:
    message = {
        'sender': row[1],
        'recipient': row[2],
        'message': row[3]
    }
    messages.append(message)

# Convert the messages to JSON format
response_data = json.dumps(messages)

# Set the response headers
print("Content-type: application/json")
print()

# Send the JSON response
print(response_data)
