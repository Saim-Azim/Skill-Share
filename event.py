#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import json
import mysql.connector

# Connect to your MySQL database
db = mysql.connector.connect(
  host='localhost',
  user='root',
  password='Sum@iy@27',
  database='skillshare'
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Get the logged-in user's username from the query parameter
params = cgi.FieldStorage()
username = params.getvalue('uname')

# Fetch the received events for the logged-in user
cursor.execute("SELECT * FROM events WHERE receiver = %s", (username,))
received_events = cursor.fetchall()

# Fetch the sent events for the logged-in user
cursor.execute("SELECT * FROM events WHERE sender = %s", (username,))
sent_events = cursor.fetchall()

# Close the database connection
db.close()

# Create a dictionary to store the received and sent events
data = {
  'receivedEvents': [],
  'sentEvents': []
}

# Iterate over the received events and convert them to a list of dictionaries
for event in received_events:
  data['receivedEvents'].append({
    'title': event[0],
    'e_date': event[1],
    'e_time': event[2],
    'sender': event[3]
  })

# Iterate over the sent events and convert them to a list of dictionaries
for event in sent_events:
  data['sentEvents'].append({
    'title': event[0],
    'e_date': event[1],
    'e_time': event[2],
    'receiver': event[4]
  })

# Return the data as a JSON response
print("Content-Type: application/json")
print()
print(json.dumps(data))
