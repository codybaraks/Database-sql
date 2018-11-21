import mysql.connector as connector
db = connector.connect(host="localhost",name="root",user="root", passwd="root",database="python")


mycursor = db.cursor()