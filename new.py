#!C:/Users/ADMIN/AppData/Local/Programs/Python/Python311/python.exe

import mysql.connector
import os
from urllib.parse import parse_qs

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sum@iy@27',
    database='skillshare'
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Prepare the SQL query to fetch data from the table
query = "SELECT b_title, b_content, username, posted_date FROM skillblog"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Get the value of the 'uname' parameter from the URL
query_string = os.environ.get('QUERY_STRING', '')
parameters = parse_qs(query_string)
uname = parameters.get('uname', [''])[0]

# Get the search input value
search_input = parameters.get('search_input', [''])[0].lower()

# Start generating the HTML content
html_content = "<div class='button-container'>"
html_content += "<a href='#' onclick='redirectToTestPage()' class='button'>Discover Skill <i class='fa fa-plus-circle' aria-hidden='true'></i></a>"
html_content += "<div style='margin-top: 10px;'></div>"  # Adding space
html_content += "<input type='text' id='search-input' placeholder='Search...' />"  # New search input
html_content += "</div>"
html_content += "<div class='blog-container'>"

# Iterate over the rows and generate HTML for each blog
for index, row in enumerate(rows):
    # Start a new row every 3 columns
    if index % 3 == 0:
        html_content += "<div class='row'>"

    html_content += "<div class='column'>"
    html_content += "<div class='blog-box'>"
    html_content += f"<h3 class='blog-title'>{row[0]}</h3><br>"

    # Check if the content is not None before splitting
    if row[1] is not None:
        content_words = row[1].split()
        limited_content = ' '.join(content_words[:10])
        if len(content_words) > 10:
            limited_content += '...'
    else:
        limited_content = "..."

    html_content += f"<p class='blog-content'>{limited_content}</p>"
    html_content += f"<p><strong>Author: {row[2]}</strong></p>"
    html_content += f"<p><strong>Posted Date: {row[3]}</strong></p>"
    html_content += f"<div class='button-container-blog'>"
    html_content += f"<a href='#' onclick='redirectToDisplayPage(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\")' class='button-blog'>View More <i class='fa fa-eye' aria-hidden='true'></i></a>"
    html_content += "</div>"
    html_content += "</div>"
    html_content += "</div>"

    # End the row after 3 columns
    if index % 3 == 2:
        html_content += "</div>"

# Close the blog container div
html_content += "</div>"

# Close the cursor and database connection
cursor.close()
connection.close()

# Print the HTML content with appropriate headers
print("Content-Type: text/html")
print()
print(html_content)
