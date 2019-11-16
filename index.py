#!/usr/bin/python3

import cgi, pymysql

form = cgi.FieldStorage()

form_name = form.getvalue("name")
form_color = form.getvalue("color")
form_cats_or_dogs = form.getvalue("cats_or_dogs")

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
<h1>My Demo</h1>
''')


db = pymysql.connect("localhost","root","thisisdemo","demo")
cursor = db.cursor()

#query_sql = "SELECT * FROM demo"
#cursor.execute(query_sql)
#records = cursor.fetchall()
#query_result = "Data:<br>"
#for row in records:
#   query_result = query_result + row[0] + "&nbsp;" * 3 + row[1] + "&nbsp;" * 3 + row[2] + "<br>"


# Insert data if all fields are non-empty
if all([form_name, form_color, form_cats_or_dogs]):
   select_sql = "SELECT * FROM demo where name = '" + form_name + "'"
   cursor.execute(select_sql)
   rows_num = cursor.rowcount

   if rows_num > 0:
      print("<p>" + form_name + " has been exist already!")
   else:
      insert_sql = "INSERT INTO demo (name, color, cats_or_dogs) VALUES ('" + form_name + "', '" + form_color + "', '" + form_cats_or_dogs + "')"
      cursor.execute(insert_sql)
      db.commit()

   db.close()



print('''
<form action="/cgi-bin/index.py" method="post">
Name: <input type="text" name="name" autofocus>
<p>Favourite Color:
<select name="color" autofocus>
<option value="Red">Red</option>
<option value="Orange">Orange</option>
<option value="Yellow">Yellow</option>
<option value="Green">Green</option>
<option value="Blue">Blue</option>
<option value="Indigo">Indigo</option>
<option value="Violet">Violet</option>
</select><br>
<p>Cats or Dogs
<input type="radio" name="cats_or_dogs" value="Cats">Cats
<input type="radio" name="cats_or_dogs" value="Dogs">Dogs
<p><input type="submit" value="Submit">
</form>
<button class="button" onClick="window.open('/cgi-bin/data.py');">
<span class="icon">Display Data</span>
</button>
</center>
</body>
</html>
''')
