import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")

mycursor = db.cursor(buffered=True )


sql = "select * FROM students WHERE names LIKE '%a%'"
#
# results=mycursor.fetchall()
mycursor.execute(sql)

result = mycursor.fetchall()
for student in result:
    print(student[1])

db.commit()
print()
print(mycursor.rowcount, "There you go")