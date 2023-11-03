#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import cgi
import mysql.connector

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Retrieve the search input from the URL parameters
form = cgi.FieldStorage()
search_input = form.getvalue('search_input', '').lower()

# Prepare the SQL query to fetch data from the table with a search condition
query = "SELECT b_title, b_content, username, posted_date FROM skillblog"
if search_input:
    query += " WHERE LOWER(b_title) LIKE '%{}%'".format(search_input)

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Generate the HTML content for the search results page
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <p>Search Input: {}</p>
""".format(search_input)

# Display the blog data if search results are available
if rows:
    for row in rows:
        html_content += "<h3>{}</h3>".format(row[0])
        html_content += "<p>{}</p>".format(row[1])
        html_content += "<p>Author: {}</p>".format(row[2])
        html_content += "<p>Posted Date: {}</p>".format(row[3])
else:
    html_content += "<p>No results found.</p>"

html_content += """
</body>
</html>
"""

# Close the cursor and database connection
cursor.close()
connection.close()

# Print the HTML content with appropriate headers
print("Content-Type: text/html")
print()
print(html_content)