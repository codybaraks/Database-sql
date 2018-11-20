import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")

mycursor= db.cursor()

mycursor.execute("select * from students limit 100")

# one = mycursor.fetchone()
#
# print(one)

results = mycursor.fetchall()

for student in results:
    if student[0] >= 1:
     print(student[1])