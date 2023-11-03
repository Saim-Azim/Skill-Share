#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get the form data
username = form.getvalue('uname')
password = form.getvalue('password')

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)
cursor = connection.cursor()

# Validate the login details
sql = "SELECT uname FROM login WHERE uname = %s AND password = %s"
values = (username, password)
cursor.execute(sql, values)
result = cursor.fetchone()

# Close the cursor and connection
cursor.close()
connection.close()

# If the login is successful, redirect to the next page with the username as a query parameter
if result:
    print("Content-type: text/html")
    print("Location: new.html?uname=" + username)
    print()
else:
    # Clear the input fields and display an error message
    print("Content-type: text/html")
    print()
    print("<html>")
    print("<head>")
    print("<title>Login Failed</title>")
    print("</head>")
    print("<body>")
    print("<script>")
    print("alert('Invalid username or password. Please try again.');")
    print("window.location = 'login.html';")  # Redirect back to the login page
    print("</script>")
    print("</body>")
    print("</html>")
