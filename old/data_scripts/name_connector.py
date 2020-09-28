#connect to mysql database with python
import mysql.connector

cnx = mysql.connector.connect(user='python', 
							  auth_plugin='mysql_native_password',
							  password = '',
                              host='localhost',
                              database='baby_names',
                              use_pure='True')
cnx.close()
