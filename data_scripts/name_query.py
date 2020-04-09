#practicing querying mysql using python

import datetime
import mysql.connector

cnx = mysql.connector.connect(user='python', database='baby_names')
cursor = cnx.cursor()

query = "SELECT name, year(year) FROM test2 WHERE year(year)='1880'"

hire_start = datetime.date(1999, 1, 1)
hire_end = datetime.date(1999, 12, 31)

#cursor.execute(query)
cursor.execute("select name,year(year) from test2 where year(year) = '1880' and name = 'zachariah'")
for (name, year) in cursor:
  print("{} was bbboorn in {}".format(
    name,year))
cursor.execute(query)
output = cursor.fetchone()
cursor.fetchall()
print(output)

cursor.close()
cnx.close()
