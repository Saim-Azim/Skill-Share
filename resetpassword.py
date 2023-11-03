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

# Get the username and new password from the form fields
username = form.getvalue('uname')
new_password = form.getvalue('newPassword')

# Check if the username exists in the login table
query = "SELECT * FROM login WHERE uname = %s"
cursor.execute(query, (username,))
result = cursor.fetchone()

if result:
    # Update the password for the username
    update_query = "UPDATE login SET password = %s WHERE uname = %s"
    cursor.execute(update_query, (new_password, username))
    db.commit()
    message = "Password updated successfully!"
    redirect_url = "login.html"  # Redirect to the login page
    alert_message = "Password reset successfully!"
else:
    message = "User details not available."
    redirect_url = "register.html"  # Redirect to the register page
    alert_message = "User details not available."

# Close the database connection
db.close()

# Print the HTTP response
print("Content-Type: text/html")
print()
print('<script>alert("{}"); window.location.href="{}";</script>'.format(alert_message, redirect_url))
