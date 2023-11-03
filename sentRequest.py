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

# Get the form data (username)
form = cgi.FieldStorage()
username = form.getvalue('uname')

# Fetch the received events from MySQL
cursor = db.cursor()
query = "SELECT title, e_date, e_time, receiver FROM events WHERE sender = %s"
cursor.execute(query, (username,))
received_events = cursor.fetchall()


# Close the database connection
db.close()

# Generate the HTML table for received events or display a message if no events
if received_events:
    table_html = '<div class="box-container">'

    for event in received_events:
        title = event[0]
        e_date = event[1]
        e_time = event[2]
        receiver = event[3]

        table_html += '<div class="box">'
        table_html += f'<p class="box-title"><strong>Title:</strong> {title}</p>'
        table_html += f'<p class="box-content"><strong>Author:</strong> {receiver}</p>'
        table_html += f'<p class="box-content"><strong>Date:</strong> {e_date}</p>'
        table_html += f'<p class="box-content"><strong>Time:</strong> {e_time}</p>'
        table_html += f'<button class="cancel-button" onclick="deleteEvent(\'{title}\')">Cancel</button>'
        table_html += '</div>'

    table_html += '</div>'
else:
    table_html = '<p>No Events Here.</p>'

# Set the response headers
print("Content-Type: text/html")
print()

# Print the HTML table or message
print(table_html)
