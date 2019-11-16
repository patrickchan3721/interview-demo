#!/usr/bin/python3

import cgi, pymysql


# Print HTML
print("Content-type:text/html\r\n\r\n")
print('''
<html>
<head>
<style>
body {
    font: 22px Arial, sans-serif;
}
</style>
</head>
<body>

<center>
<h1>Display Data</h1>
''')


db = pymysql.connect("localhost","root","thisisdemo","demo")
cursor = db.cursor()

query_sql = "SELECT * FROM demo"
cursor.execute(query_sql)
records = cursor.fetchall()
query_result = "<br><table border=1>"
for row in records:
   query_result = query_result + "<tr><td>" + row[0] + "&nbsp;" * 3 + "</td><td>" + row[1] + "&nbsp;" * 3 + "</td><td>" + row[2] + "&nbsp;" * 3 + "</td></tr>"

db.close()

print("</table><p><p>")
print(query_result)
print('''
<p><p>
<button value="Refresh" onClick="window.location.reload();">
Refresh
</button>
</center>
</body>
</html>
''')
