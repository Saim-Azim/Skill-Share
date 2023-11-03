#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get the form data
b_title = form.getvalue('b_title')
b_category = form.getvalue('b_category')
b_content = form.getvalue('b_content')
username = form.getvalue('uname')

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)
cursor = connection.cursor()

# Check if the blog data already exists
query = "SELECT * FROM skillblog WHERE b_title = %s AND category = %s AND b_content = %s AND username = %s"
values = (b_title, b_category, b_content, username)
cursor.execute(query, values)
result = cursor.fetchone()

if result:
    # If the data already exists, display an error message and refresh the page
    print("Content-type: text/html")
    print("Refresh: 5;url=new.html?uname=" + username)  # Refresh the page after 5 seconds
    print()
    print("<html>")
    print("<head>")
    print("<title>Error</title>")
    print("</head>")
    print("<body>")
    print("<h1>Error: Duplicate Data</h1>")
    print("<p>The blog data you entered already exists.</p>")
    print("<p>You will be redirected back to the blog creation page shortly.</p>")
    print("</body>")
    print("</html>")
else:
    # If the data does not exist, insert it into the skillblog table
    insert_query = "INSERT INTO skillblog (b_title, category, b_content, username) VALUES (%s, %s, %s, %s)"
    insert_values = (b_title, b_category, b_content, username)
    cursor.execute(insert_query, insert_values)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Redirect to the new.html page
    print("Content-type: text/html")
    print("Location: new.html?uname=" + username)
    print()
