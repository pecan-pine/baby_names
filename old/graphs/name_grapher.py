import matplotlib.pyplot as plt
import mysql.connector

cnx = mysql.connector.connect(user='python', database='baby_names')
cur = cnx.cursor()
name=str(input('what is your name'))
gender = str(input('what is your gender?'))
command = "SELECT year(year), frequency FROM test2 WHERE name='"+name+"' AND sex='"+gender+"';"
cur.execute(command)
data=cur.fetchall()
x_val = [x[0] for x in data]
y_val = [x[1] for x in data]
fig=plt.figure(figsize=(5,5))
plt.plot(x_val,y_val, label="Name="+name+", Gender="+gender)
plt.legend(fontsize=12)
ax=fig.add_subplot(111)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of people', fontsize=12)
plt.show()