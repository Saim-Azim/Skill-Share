#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector
import sys

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Prepare the SQL queries
check_username_query = "SELECT * FROM login WHERE uname = %s"
check_email_query = "SELECT * FROM login WHERE email = %s"
insert_user_query = "INSERT INTO login (uname, email, password) VALUES (%s, %s, %s)"

# Get the form data from the request
form = cgi.FieldStorage()
name = form.getvalue('uname')
email = form.getvalue('email')
password = form.getvalue('password')

# Check if the username already exists
cursor.execute(check_username_query, (name,))
existing_username = cursor.fetchone()

# Check if the email already exists
cursor.execute(check_email_query, (email,))
existing_email = cursor.fetchone()

# If username or email already exists, show a message and abort
if existing_username or existing_email:
    print("Content-Type: text/html")
    print()
    print("<script>")
    print("alert('Registration Failed: Username or Email already exists. Please choose a different one.');")
    print("window.location.href = 'register2.html';")  # Redirect back to the registration page
    print("</script>")
    sys.stdout.flush()
    cursor.close()
    connection.close()
    sys.exit(0)

# Insert user data into the table
cursor.execute(insert_user_query, (name, email, password))

# Get the generated user ID (u_id)
u_id = cursor.lastrowid

# Commit the changes to the database
connection.commit()

# Close the cursor and database connection
cursor.close()
connection.close()

# Redirect to the next page
next_page_url = 'login.html'
print('Content-Type: text/html')
print('Location: ' + next_page_url)
print()
sys.stdout.flush()
